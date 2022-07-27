from django.test import TestCase
from django.urls import reverse, resolve
from .forms import BookingForm
# Create your tests here.

class TestBookingForm(TestCase):

    def test_booking_name_is_required(self):
        form = BookingForm({'customer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('customer', form.errors.keys())
        self.assertEqual(form.errors['customer'][0], 'This field is required.')

    def test_booking_people_is_required(self):
        form = BookingForm({'people': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors.keys())
        self.assertEqual(form.errors['people'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['customer', 'people', 'phone_number', 'booking_date', 'booking_time'])