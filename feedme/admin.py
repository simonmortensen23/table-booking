"""
Representation of the booking model in the admin interface.
"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Class registered to represent model in admin database.
    """
    list_display = ('user', 'customer',
                    'booking_date', 'booking_time',
                    'phone_number',
                    'people')
    search_fields = ('customer',
                     'booking_date', 'booking_time',
                     'phone_number')
    list_filter = ('customer',
                   'booking_date', 'booking_time',
                   'phone_number')
