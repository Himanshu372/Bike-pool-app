from django.db import models

# Create your models here.
from django.db import models
import datetime


class rideData(models.Model):
    user_id = models.CharField(max_length = 50, null=False)
    pickup = models.CharField(max_length=1000, null=False)
    dropoff = models.CharField(max_length=1000, null=False)
    stopovers = models.CharField(max_length=1000, null=False)
    depart_time = models.DateTimeField(auto_now=False, auto_now_add=False, null = False)
    return_time = models.DateTimeField(auto_now=False, auto_now_add=False, null = True)
    is_return = models.BooleanField(default = False)

    # def __str__(self):
    #     return 'Ride starts from {} at {} and ends at {} with stopovers at {}'.format(self.pickup, datetime.datetime(self.depart_time).time(), self.dropoff, )


