from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from travels.models import TravelOption
from .models import Booking

class BookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Testpass123!')
        self.travel = TravelOption.objects.create(
            type='Bus',
            source='A',
            destination='B',
            date_time='2030-01-01T10:00:00Z',
            price=50.00,
            available_seats=5
        )

    def test_booking_create(self):
        self.client.login(username='testuser', password='Testpass123!')
        response = self.client.post(reverse('bookings:booking_create', args=[self.travel.travel_id]), {
            'number_of_seats': 2
        })
        self.assertEqual(response.status_code, 302)
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.number_of_seats, 2)
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 3)

    def test_booking_cancel(self):
        self.client.login(username='testuser', password='Testpass123!')
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=2,
            total_price=100.00,
            status='Confirmed'
        )
        response = self.client.post(reverse('bookings:booking_cancel', args=[booking.booking_id]))
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.status, 'Cancelled')
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 5)
