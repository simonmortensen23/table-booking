from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .models import Booking
from .views import make_booking, view_booking, edit_booking, delete_booking
# Create your tests here.

class TestViews(TestCase):
    
    @classmethod
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='test@test.org', username='john', password='Test!2345')

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

    # def test_get_edit_booking(self):
    #     booking = Booking.objects.create(customer='Test Costumer')
    #     request = self.factory.get(f'/edit/{booking.id}')
    #     request.user = self.user
    #     customer = 'Test customer 2'
    #     self.assertEqual(len(existing_booking), 0)

    # def test_can_delete_booking(self):
    #     booking = Booking.objects.create(customer='Test Costumer')
    #     request = self.factory.get(f'/delete/{booking.id}')
    #     request.user = self.user
    #     existing_booking = Booking.objects.filter(id=booking.id)
    #     self.assertEqual(len(existing_booking), 0)
        