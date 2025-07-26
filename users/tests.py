from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile
from products.models import Product, Category
from unittest.mock import patch

# Create your tests here.

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        self.category = Category.objects.create(name='TestCat')
        self.product = Product.objects.create(name='TestProduct', description='desc', price=10, category=self.category)

    def test_registration_creates_user_and_profile(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after registration
        user = User.objects.get(username='testuser')
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_login(self):
        user = User.objects.create_user('loginuser', 'login@example.com', 'loginpass')
        response = self.client.post(reverse('login'), {'username': 'loginuser', 'password': 'loginpass'})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        user = User.objects.create_user('profileuser', 'profile@example.com', 'profilepass')
        self.client.login(username='profileuser', password='profilepass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_access(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TestProduct')

class WelcomeEmailTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('users.utils.send_welcome_email')
    def test_welcome_email_sent_on_registration(self, mock_send_email):
        response = self.client.post(reverse('register'), {
            'first_name': 'Email',
            'last_name': 'Test',
            'username': 'emailtestuser',
            'email': 'emailtestuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
        })
        self.assertEqual(response.status_code, 302)
        mock_send_email.assert_called_once_with('emailtestuser@example.com', 'Email')
