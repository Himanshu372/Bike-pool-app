from django.shortcuts import render
from bike_app.models import rideData
from bike_app.serializers import rideDataSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from bike_app.forms import findRideform, offerRideform
from django.http import HttpRequest,HttpResponse
from rest_framework.views import APIView


# Create your views here.



def home(request):
    return render(request, 'bike_app/index.html')


class fetchrideData(viewsets.ModelViewSet):
    queryset = rideData.objects.all()
    template_name = 'bike_app/offer_ride.html'


    def create(self, request, *args, **kwargs):
        post_data = request.data
        serializer = rideDataSerializer(data = post_data)
        user_id = post_data['user_id']
        depart_time = post_data['depart_time']
        if self.queryset.filter(user_id = user_id, depart_time = depart_time).exists():
            return Response('You have already created a ride for given departure time')
        else:
            if serializer.is_valid():
                serializer.save()
                return Response('Your ride has been saved, expect bookings anytime')
            else:
                return Response('Please check your data')

    def list(self, request, format = None):
        form = offerRideform()
        args = {'form' : form}
        return render(request, self.template_name, args)


def offerRide(request):
    if request.method == 'POST':

        data = request.POST
        pickup = data['pickup']
        dropoff = data['dropoff']
        stopover_list = []
        for i in range(0, len(data) - 3):
            stopover_list.append(data['stopover_' + str(i)])
        print(stopover_list)



    elif request.method == 'GET':
        form = offerRideform()
        args = {'form': form}
        return render(request,'bike_app/offer_ride.html', args)








def getRideDetails(request):
    formDate = findRideform(request.POST)
    ridersData = rideData.objects.filter()



















