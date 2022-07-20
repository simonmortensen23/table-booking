from django.shortcuts import render
from django.views import generic
from .models import Restaurant
# Create your views here.

class RestaurantView(generic.ListView):
    model = Restaurant
