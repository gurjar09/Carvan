from django.db import models

# Create your models here.

class HostDetails(models.Model) :
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()
   

class HostDocument(models.Model) :
    adhar_card = models.ImageField(upload_to='documents/adhar')
    driving_license = models.ImageField(upload_to='documents/DL')
    registration_card = models.ImageField(upload_to='documents/RC')
    puc_card = models.ImageField(upload_to='documents/PUC')
    car_insurance = models.ImageField(upload_to='documents/Incurance')

class AddCar(models.Model):
    carName = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    seat = models.IntegerField()
    fuel_types = [
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('CNG', 'CNG')
    ]
    fuel_type = models.CharField(max_length=10, choices=fuel_types)
    transmission_types = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    ]
    transmission_type = models.CharField(max_length=10, choices=transmission_types)


class CarImage(models.Model):
    car = models.ForeignKey(AddCar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"Image for {self.car.carName}"


class Booking(models.Model):
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()
    car = models.ForeignKey(AddCar, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking from {self.pickup_location} to {self.dropoff_location}"
