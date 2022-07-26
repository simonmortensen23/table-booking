from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_home, name='home'),
    path('menu/', views.view_menu, name='menu'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
]