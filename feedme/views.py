from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant
# Create your views here.

class RestaurantView(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    template_name = "index.html"
