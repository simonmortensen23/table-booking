from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=250, default='Restaurant', unique=True)
    description = models.CharField(max_length=250, default='Restaurant')
    opening_time = models.IntegerField(default=0)
    closing_time = models.IntegerField(default=0)


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    size = models.IntegerField()


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
    

class Meta:
    ordering = ['-title']

def __str__(self):
    return self.title