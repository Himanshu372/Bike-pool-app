from rest_framework import serializers
from bike_app.models import rideData
from django.core.serializers.json import Serializer



class rideDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = rideData
        fields = ['user_id', 'pickup', 'dropoff', 'stopovers', 'depart_time', 'return_time', 'is_return']


class findRideResponseSerializer(Serializer):
    def get_dump_object(self, obj):
        mapped_obj = {
            'user_id' : obj.user_id,
            'distance' : obj.distance,
            'depart_time' : obj.depart_time,
            'fare' : obj.fare
        }
        return mapped_obj
