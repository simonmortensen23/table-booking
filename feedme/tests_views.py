'''
Test cases for applications different views
and the users access to the views
'''
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Booking
from .views import make_booking, view_booking, edit_booking
# Create your tests here.


class TestViews(TestCase):
    '''
    Setup for test user for pages that require
    login access
    '''
    @classmethod
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            email='test@test.org', username='john', password='Test!2345')

    def test_get_home_page(self):
        print('Test Home Page')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_menu_page(self):
        print('Test Menu')
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_get_edit_booking_page(self):
        print('Edit Bookings')
        booking = Booking.objects.create(customer='Test Costumer')
        request = self.factory.get(f'/edit/{booking.id}')
        request.user = self.user
        response = edit_booking(request, booking_id=1)
        self.assertEqual(response.status_code, 200)

    def test_get_make_booking_page(self):
        print('Make Bookings')
        booking = Booking.objects.create(customer='Test Costumer')
        request = self.factory.get('/make_booking/')
        request.user = self.user
        response = make_booking(request)
        self.assertEqual(response.status_code, 200)

    def test_get_view_booking(self):
        print('View Bookings')
        request = self.factory.get('/view_booking/')
        request.user = self.user
        response = view_booking(request)
        self.assertEqual(response.status_code, 200)
