from django.shortcuts import render
from bike_app.models import rideData
from bike_app.serializers import rideDataSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from bike_app.forms import findRideform
from django.http import HttpRequest,HttpResponse
from rest_framework.views import APIView
from bike_app.processing_data import get_location, cal_haversine_distance
from datetime import datetime





def home(request):
    return render(request, 'bike_app/index.html')


class offerRide(viewsets.ModelViewSet):
    queryset = rideData.objects.all()
    template_name = 'bike_app/offer_ride.html'


    def create(self, request, *args, **kwargs):
        # try:
        data = request.POST
        pickup = data['pickup']
        dropoff = data['dropoff']

        # Should add a validation check here
        pickup_lat_long = get_location(pickup)
        dropoff_lat_long = get_location(dropoff)
        date_time = data['datetimepicker']
        date_time_field = datetime.strftime(datetime.strptime(date_time, '%m/%d/%Y %H:%M %p'),'%Y-%m-%d %H:%M:%S')
        stopover_list = []
        for i in range(0, len(data) - 4):
            stopover_list.append(data['stopover_' + str(i)])
        stopover_lat_long_list = [str(get_location(k)) for k in stopover_list]
        rideData_obj = rideData(user_id = 101, pickup = str(pickup_lat_long), dropoff = str(dropoff_lat_long), stopovers = ''.join(stopover_lat_long_list), depart_time = date_time_field)
        if self.queryset.filter(user_id = 101, pickup = str(pickup), depart_time = date_time_field).exists():
            pass
        else:
            rideData_obj.save()
            return HttpResponse('Success')
        # except:
        #     return HttpResponse('Please check your input data')

    def list(self, request):
        return render(request, self.template_name)





# def findRide(request):
#     form = findRideform()
#     args = {'form' : form}
#     if request.method == 'GET':
#         return render(request, 'bike_app/find_ride.html',args)
#
#     elif request.method == 'POST':
#         pickup = request.POST['pickup']
#         geolocation = get_location(pickup)
#         return HttpResponse('Success')


class findRide(viewsets.ModelViewSet):
    queryset = rideData.objects.all()
    template_name = 'bike_app/find_ride.html'

    def list(self, request, *args, **kwargs):
        form = findRideform
        args = {'form' : form}
        return render(request, self.template_name, args)

    def create(self, request, *args, **kwargs):
        data = request.POST
        pickup_loc = data['pickup']
        dropoff_loc = data['dropoff']
        travel_date = data['date']
        travel_time = data['time']
        travel_date_time = datetime.strftime(datetime.strptime(travel_date + ' ' + travel_time, '%Y-%m-%d %H:%M'),'%Y-%m-%d %H:%M:%S')

        # Should include a validation check here
        pickup_lat_long = get_location(pickup_loc)
        dropoff_lat_long = get_location(dropoff_loc)
        rides = self.queryset.filter(depart_time__date = travel_date)
        results = {}
        for each_ride in rides:
            dist = cal_haversine_distance(str(pickup_lat_long), each_ride.pickup)
            results[each_ride.user_id] = {}
            results[each_ride.user_id]['distance'] = dist
            results[each_ride.user_id]['depart_time'] = datetime.strftime(each_ride.depart_time.date(), '%Y-%m-%d')
            results[each_ride.user_id]['fare'] = round(50 + 12 * dist)
        results = sorted(results.items(), key = lambda x : x[1]['distance'], reverse = True)
        return HttpResponse(results)

















