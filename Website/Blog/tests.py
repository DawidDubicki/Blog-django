from django.test import TestCase
from django.urls import reverse
from .models import User


class AccountTests(TestCase):
    def setUp(self):
        self.register_url = reverse('register_url')
        self.login_url = reverse('login_url')
        self.register_url_response = self.client.get(self.register_url)
        self.login_url_response = self.client.get(self.login_url)
        self.register_data = {'username': 'test', 'password': 'test', 'password_repeat': 'test'}
        self.login_data = {'username': 'test', 'password': 'test'}

    # register test cases
    def test_register_url_response(self):
        self.assertEqual(self.register_url_response.status_code, 200)

    def test_register_template_used(self):
        self.assertTemplateUsed(self.register_url_response, 'register.html')

    def test_account_creation(self):
        self.account_creation_response = self.client.post(reverse('register_url'), self.register_data)
        self.assertEqual(self.account_creation_response.status_code, 302)
        self.assertEqual(User.objects.get(username='test').username, 'test')

    # login test cases
    def test_login_url_response(self):
        self.assertEqual(self.login_url_response.status_code, 200)

    def test_login_template_used(self):
        self.assertTemplateUsed(self.login_url_response, 'login.html')

    def test_login_login(self):
        self.login_url_login_response = self.client.post(reverse('login_url'), self.login_data)
        self.assertEqual(self.login_url_login_response.status_code, 200)

