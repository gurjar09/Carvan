from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import AddCar, Booking
from django.http import JsonResponse


def index(request):
    carvanVehicle = AddCar.objects.all()
    
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        pickup_time = request.POST.get('pickup_time')
        dropoff_time = request.POST.get('dropoff_time')
        car_id = request.POST.get('car_id')
        
        car = AddCar.objects.get(id=car_id)
        
        Booking.objects.create(
            pickup_location=pickup_location,
            pickup_date=pickup_date,
            return_date=return_date,
            pickup_time=pickup_time,
            dropoff_time=dropoff_time,
            car=car
        )
        return redirect('booking_success')
    
    return render(request, 'index.html', {'carvanVehicle': carvanVehicle})

# def booking_success(request):
#     return render(request, 'booking_success.html')

def get_location(request):
    if request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        if latitude and longitude:
            response = requests.get(
                f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={settings.YOUR_GOOGLE_API_KEY}'
            )
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    address = data['results'][0]['formatted_address']
                    return JsonResponse({'status': 'success', 'address': address})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Unable to fetch address'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Error calling geocoding API'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def about(request) :
    return render(request,'about.html')

def services(request) :
    return render(request,'services.html')



def cars_list(request):
    cars = AddCar.objects.all()

    # Get filter parameters from request
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    fuel_type = request.GET.get('fuel_type')
    transmission_type = request.GET.get('transmission_type')

    # Apply filters if they exist
    if brand:
        cars = cars.filter(brand=brand)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)
    if transmission_type:
        cars = cars.filter(transmission_type=transmission_type)

    return render(request, 'car.html', {'carvanVehicle': cars})
    

def contact(request):
    return render(request,'contact.html')


def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect(index)
        else :
            messages.success(request,("Please enter an Correct Username & Password..."))
    return render(request,'login.html')

def signup(request) :
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        data.save()
        return redirect(login)
    else :
        messages.success(request,("You're Register SuccessFull..."))

    return render(request,'signup.html')

def host(request) :
    if request.method == 'POST' :
        owner_first_name = request.POST.get('owner_first_name')
        owner_last_name = request.POST.get('owner_last_name')
        mobile_number = request.POST.get('mobile_number')
        email_address = request.POST.get('email_address')
        data = HostDetails(owner_first_name = owner_first_name,owner_last_name=owner_last_name,mobile_number=mobile_number,email_address=email_address)
        data.save()
        
        return redirect(document)
    HostDoc = HostDetails.objects.all()
    return render(request,'Host.html',{'HostDoc' : HostDoc})


def document(request) :
    if request.method == 'POST' :
        adhar_card = request.FILES.get('adhar_card')
        driving_license = request.FILES.get('driving_license')
        registration_card = request.FILES.get('registration_card')
        puc_card = request.FILES.get('puc_card')
        car_insurance = request.FILES.get('car_insurance')
        data = HostDocument(adhar_card=adhar_card,driving_license=driving_license,registration_card=registration_card,puc_card=puc_card,car_insurance=car_insurance)
        data.save()
        return redirect(hostCarDetails)
        
    return render(request,'hostDocument.html')


def hostCarDetails(request):
    if request.method == 'POST':
        try:
            # Collect car details from POST request
            carName = request.POST.get('carName')
            brand = request.POST.get('brand')
            price = request.POST.get('price')
            mileage = request.POST.get('mileage')
            seat = request.POST.get('seat')
            fuel_type = request.POST.get('fuel_type')
            transmission_type = request.POST.get('transmission_type')

            # Create a new AddCar instance
            car = AddCar.objects.create(
                carName=carName,
                brand=brand,
                price=price,
                mileage=mileage,
                seat=seat,
                fuel_type=fuel_type,
                transmission_type=transmission_type
            )

            # Collect images from the request
            images = request.FILES.getlist('images')
            for image in images:
                CarImage.objects.create(car=car, image=image)

            # Redirect to a success page or the car list page
            return redirect(cars_list)  # Assuming 'car_list' is the name of your URL pattern for listing cars

        except Exception as e:
            # Handle any exception that occurs during car creation or image upload
            if 'car' in locals():
                car.delete()  # Optionally, delete the car object if it was created
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

    return render(request, 'hostCarDetails.html')  # Render the car creation template

def car_single(request, car_id):
    car = get_object_or_404(AddCar, id=car_id)
    return render(request, 'car-single.html', {'car': car})


# def profile(request) :
#     user = request.user
#     cars = AddCar.objects.filter(rented_by=user)
#     return render(request, 'profile.html', {'cars': cars})
