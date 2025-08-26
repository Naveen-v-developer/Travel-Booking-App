from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_register(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Testpass123!')

    def test_profile_update(self):
        self.client.login(username='testuser', password='Testpass123!')
        response = self.client.post(reverse('users:profile'), {
            'username': 'testuser2',
            'email': 'new@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'testuser2')
