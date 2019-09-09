from rest_framework import serializers
from bike_app.models import rideData



class rideDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = rideData
        fields = ['user_id', 'pickup', 'dropoff', 'stopovers', 'depart_time', 'return_time', 'is_return']
