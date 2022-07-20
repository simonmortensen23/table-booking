from django.urls import path
from feedme.views import RestaurantView

urlpatterns = [
    path('restaurants/', RestaurantView.as_view(), name='home')
]