from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_home, name='home'),
    path('booking/', views.booking, name='booking'),
]