from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant
# Create your views here.

class RestaurantView(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.order_by('-name')
    template_name = "index.html"

    def index(request):
        restaurant_list = Restaurant.objects.order_by('-name')
        context = {'restaurant_list': restaurant_list}
        return render(request, 'index.html', context)