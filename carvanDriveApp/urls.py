from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('about-us/', about, name='about'),
    path('services/', services, name='services'),
    path('pricing/', pricing, name='pricing'),
    path('car/', cars_list, name='car'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('host/', host, name='host'),
    path('document/', document, name='document'),
    path('host-car-details/', hostCarDetails, name='hostCarDetails'),
    path('car-single/<int:car_id>/', car_single, name='car_single'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
