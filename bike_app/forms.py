from django import forms
from bike_app.models import rideData
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

class findRideform(forms.Form):
    pickup = forms.CharField(max_length = 1000, label = 'Pickup point')
    dropoff = forms.CharField(max_length = 1000, label = 'Dropping point')
    date = forms.CharField(max_length = 10, label = 'Date', widget = forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    date = forms.DateField(widget = DatePickerInput(format='YYYY-MM-DD'))
    time = forms.DateField(widget = TimePickerInput())










