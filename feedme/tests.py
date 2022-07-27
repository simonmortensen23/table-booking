from django.test import TestCase
from django.urls import reverse, resolve
from .models import Booking
from .views import make_booking, view_booking, edit_booking, view_home, view_menu
# Create your tests here.

class TestDjango(TestCase):

    def test_try_test(self):
        self.assertEqual(1, 1)