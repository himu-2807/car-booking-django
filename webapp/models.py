from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Contact(models.Model):
    cname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    message=models.TextField()

class Car(models.Model):
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=50, help_text="e.g. SUV, Sedan, Hatchback")
    price_per_day = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars/')   # requires Pillow
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ₹{self.price_per_day}/day"
    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'price_per_day')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.car_name}"
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car_name', 'pickup_date', 'return_date', 'pickup_location', 'booked_on')