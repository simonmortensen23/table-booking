from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Costumer(models.Model):
    name = models.CharField(max_length=50, default='Costumer')
    email = models.EmailField(unique=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=250, default='Restaurant', unique=True)
    description = models.CharField(max_length=250, default='Restaurant')
    image = CloudinaryField('image', default='Placeholder')
    opening_time = models.IntegerField(default=0)
    closing_time = models.IntegerField(default=0)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    size = models.IntegerField()


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
    

