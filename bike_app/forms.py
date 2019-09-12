from django import forms

class findRideform(forms.Form):
    pickup = forms.CharField(max_length = 1000, label = 'Pickup', )
    dropoff = forms.CharField(max_length = 1000, label = 'Dropoff')
    date = forms.CharField(max_length = 10, label = 'Date', widget = forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    time = forms.CharField(max_length = 10, label = 'Time', widget = forms.TextInput(attrs={'placeholder': 'hh:mm:ss'}))





