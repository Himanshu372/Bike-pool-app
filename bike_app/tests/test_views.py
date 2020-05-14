from django.test import TestCase, Client
from django.urls import reverse
from ..forms import userSignup


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bike_app/index.html')


class TestUserLoginView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_login_get(self):
        get_response = self.client.get(reverse('login'))
        self.assertEqual(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'bike_app/login.html')


class TestUserSignUpView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_signup_get(self):
        get_response = self.client.get(reverse('signup'))
        form_data = {'firstname': 'Babu', 'lastname': 'Bhatt',
                     'email': 'babubhatt09gmail.com', 'password': 'kewt5447'}
        form = userSignup(data=form_data)
        self.assertEqual(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'bike_app/signup.html')
        self.assertTrue(form.is_valid())