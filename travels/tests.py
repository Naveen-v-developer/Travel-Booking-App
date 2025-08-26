from django.test import TestCase
from django.urls import reverse
from .models import TravelOption

class TravelOptionTest(TestCase):
    def setUp(self):
        self.travel = TravelOption.objects.create(
            type='Flight',
            source='A',
            destination='B',
            date_time='2030-01-01T10:00:00Z',
            price=100.00,
            available_seats=10
        )

    def test_travel_list(self):
        response = self.client.get(reverse('travels:travel_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Flight')

    def test_travel_detail(self):
        response = self.client.get(reverse('travels:travel_detail', args=[self.travel.travel_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A')
