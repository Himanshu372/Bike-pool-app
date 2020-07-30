from datetime import datetime
import json

from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from bike_app.models import rideData, user
from bike_app.serializers import rideDataSerializer, findRideResponseSerializer
from bike_app.response_classes import FindRideResponse, FindRideResponseEncode
from bike_app.forms import findRideform, userLogin, userSignup
from bike_app.processing_data import get_location, cal_haversine_distance





def home(request):
    return render(request, 'bike_app/index.html')


class UserLogin(viewsets.ModelViewSet):
    queryset = user.objects.all()
    template_name = 'bike_app/login.html'
    login_form = userLogin()

    def list(self, request, *args, **kwargs):
        login_form = self.login_form
        args = {'form': login_form}
        return render(request, self.template_name, args)

class UserSignup(viewsets.ModelViewSet):
    queryset = user.objects.all()
    template_name = 'bike_app/signup.html'
    signup_form = userSignup()

    def list(self, request, *args, **kwargs):
        signup_form = self.signup_form
        args = {'form': signup_form}
        return render(request, template_name=self.template_name, context=args)

    def create(self, request, *args, **kwargs):
        # try:
        data = request.POST
        user_email = data['email']
        user_firstname = data['firstname']
        user_lastname = data['lastname']
        user_password = make_password(data['password'])
        if self.queryset.filter(email=user_email).exists():
            messages.info(request, 'This email id already exists, kindly enter a different address')
            return redirect('/signup')
        else:
            new_user = user(first_name=user_firstname, last_name=user_lastname,
                            email=user_email, password=user_password)
            new_user.save()
            messages.info(request, 'Thanks for signing in!')
            return redirect('/')
        # except:
        #     return Response('Form data not valid')

class OfferRide(viewsets.ModelViewSet):
    queryset = rideData.objects.all()
    template_name = 'bike_app/offer_ride.html'

    def create(self, request, *args, **kwargs):
        # try:
        data = request.POST
        depart = data['depart']
        arrival = data['arrival']
        is_return = getattr(data, 'is_return', False)
        # Should add a validation check here
        depart_lat_long = get_location(depart)
        arrival_lat_long = get_location(arrival)
        if is_return:
            depart_date_time = data['datetimepicker-departure']
            arrival_date_time = data['datetimepicker-arrival']
            depart_date_time_field = datetime.strftime(datetime.strptime(depart_date_time, '%m/%d/%Y %H:%M %p'),
                                                       '%Y-%m-%d %H:%M:%S')
            arrival_date_time_field = datetime.strftime(datetime.strptime(arrival_date_time, '%m/%d/%Y %H:%M %p'),
                                                       '%Y-%m-%d %H:%M:%S')
        else:
            depart_date_time = data['datetimepicker-departure']
            depart_date_time_field = datetime.strftime(datetime.strptime(depart_date_time, '%m/%d/%Y %H:%M %p'),
                                                       '%Y-%m-%d %H:%M:%S')
            arrival_date_time_field = None
        stopovers = getattr(data, 'stopover_0', None)
        if stopovers:
            stopover_list = []
            for i in range(0, len(data) - 6):
                stopover_list.append(data['stopover_' + str(i)])
            stopover_lat_long_list = [str(get_location(k)) for k in stopover_list]
            stopovers = stopover_lat_long_list
        ride_data_obj = rideData(user_id=21, pickup=str(depart_lat_long),
                                 dropoff=str(arrival_lat_long), stopovers=str(stopovers),
                                 depart_time=depart_date_time_field, return_time=arrival_date_time_field,
                                 is_return=is_return)
        if self.queryset.filter(user_id=21, pickup=str(depart_lat_long),
                                depart_time=depart_date_time_field).exists():
            return HttpResponse('A similar ride already exists')
        else:
            ride_data_obj.save()
            return HttpResponse('Success')
        # except:
        #     return HttpResponse('Please check your input data')

    def list(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FindRide(viewsets.ModelViewSet):
    queryset = rideData.objects.all()
    template_name = 'bike_app/find_ride.html'

    def list(self, request, *args, **kwargs):
        form = findRideform
        args = {'form': form}
        return render(request, template_name=self.template_name, context=args)

    def create(self, request, *args, **kwargs):
        data = request.POST
        pickup_loc = data['pickup']
        dropoff_loc = data['dropoff']
        travel_date_time = data['datetime']
        date_time_obj = datetime.strptime(travel_date_time, '%m/%d/%Y %H:%M %p')

        # Should include a validation check here
        pickup_lat_long = get_location(pickup_loc)
        dropoff_lat_long = get_location(dropoff_loc)
        rides = self.queryset.filter(depart_time__date=date_time_obj.date())
        results = []
        for i, each_ride in enumerate(rides):
            pickup_dist = cal_haversine_distance(str(pickup_lat_long), each_ride.pickup)
            dropoff_dist = cal_haversine_distance(str(dropoff_lat_long), each_ride.dropoff)
            distance_travelled = cal_haversine_distance(each_ride.pickup, each_ride.dropoff)
            respone_obj = FindRideResponse(user_id=21, distance=pickup_dist,
                                           depart_time=datetime.strftime(each_ride.depart_time.date(), '%Y-%m-%d'),
                                           fare=round(50 + 12 * distance_travelled))
            results.append(respone_obj)
        results = sorted(results, key=lambda x: x.distance, reverse=True)
        response = {i: vars(ride) for i, ride in enumerate(results)}
        if results:
            return Response(data=response, status=201)
        else:
            return Response('No Rides found')


class ShowRides(viewsets.ModelViewSet):
    template_name = 'bike_app/show_rides.html'

    def list(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)










