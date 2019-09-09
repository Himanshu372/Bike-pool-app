from django.shortcuts import render
from bike_app.models import rideData
from bike_app.serializers import rideDataSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.



def home(request):
    return render(request, 'bike_app/index.html')


class fetchrideData(viewsets.ModelViewSet):
    queryset = rideData.objects.all()


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








