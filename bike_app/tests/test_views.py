import mock
from mock import Mock
from django.test import TestCase, Client
from django.urls import reverse
from ..forms import userSignup, findRideform
from ..models import rideData
from ..views import OfferRide, FindRide

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
        self.form_data = {'firstname': 'Babu', 'lastname': 'Bhatt',
                            'email': 'babubhatt09@gmail.com', 'password': 'kewt5447'}

    def test_user_signup_get(self):
        get_response = self.client.get(reverse('signup'))
        form = userSignup(data=self.form_data)
        self.assertEqual(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'bike_app/signup.html')
        self.assertTrue(form.is_valid())

    # def test_user_signup_post(self):
    #     post_response = self.client.post(path=reverse('signup'), data=self.form_data)
    #     self.assertRedirects(post_response, '')


class TestOfferRideViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_data = {'depart': 'Bremen Chowk, Vidyapeeth Road, Pune University, Aundh, Pune, Maharashtra, India',
                          'arrival': 'B.A.R.C, Trombay, Mumbai, Maharashtra, India',
                          'is_return': '',
                          'stopover_0': '',
                          'datetimepicker-departure': '05/17/2020 12:00 PM'}

    def test_offer_ride_post_success(self):
        post_response = self.client.post(reverse('offer_ride'), data=self.post_data)
        self.assertEqual(post_response.status_code, 200)

    @mock.patch.object(OfferRide.queryset, 'filter')
    def test_offer_ride_post_object_exists(self, mock_filter):
        mock_filter.return_value.exists.return_value = True
        post_response_with_existing_object = self.client.post((reverse('offer_ride')), data=self.post_data)
        self.assertEqual(post_response_with_existing_object.content.decode('utf-8'), 'A similar ride already exists')

    def test_offer_ride_get_success(self):
        get_response = self.client.get(reverse('offer_ride'))
        self.assertTemplateUsed(get_response, 'bike_app/offer_ride.html')


class TestFindRideViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_data = {'pickup': 'Bremen Chowk, Vidyapeeth Road, Pune University, Aundh, Pune, Maharashtra, India',
                          'dropoff': 'B.A.R.C, Trombay, Mumbai, Maharashtra, India',
                          'datetime': '05/17/2020 12:00 PM'
        }

    def test_find_ride_get_success(self):
        get_response = self.client.get(reverse('find_ride'))
        self.assertEqual(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'bike_app/find_ride.html')

    def test_find_ride_post_success(self):
        post_response = self.client.post(reverse('find_ride'), data=self.post_data)
        self.assertEqual(post_response.status_code, 200)

    @mock.patch.object(FindRide.queryset, "filter")
    def test_find_ride_post_no_ride_found(self, mock_filter):
        mock_filter.return_value = []
        post_response = self.client.post(reverse('find_ride'), data=self.post_data)
        self.assertEqual(post_response.json(), 'No Rides found')