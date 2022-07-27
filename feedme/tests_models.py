from django.test import TestCase
from django.utils import timezone
from django.urls import reverse, resolve
from .models import Booking
# Create your tests here.

class TestModels(TestCase):

    def test_booking_str(self):
        print('Test __str__')
        booking = Booking.objects.create(
            customer='john', people='5', booking_date='2023-01-01')
        self.assertEqual(str(booking), 'john has made a booking for 5 customers for 2023-01-01.')

    # def test_validate_date(self):
    #     print('Validate date')
    #     booking = Booking.objects.create(booking_date='2022-01-01')
    #     self.assertTrue(booking, timezone.now)
       
