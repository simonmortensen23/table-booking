from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Table(models.Model):
    size = models.IntegerField()


class Booking(models.Model):
    costumer = models.TextField(max_length=250, default='costumer')
    email = models.EmailField(max_length=250, default='email')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
