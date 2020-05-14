from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from bike_app.models import user

class findRideform(forms.Form):
    pickup = forms.CharField(max_length=1000, label='Pickup point',
                             widget=forms.TextInput(attrs={'placeholder': 'Pickup', 'class': 'pickup-textbox'}))
    dropoff = forms.CharField(max_length=1000, label='Dropping point',
                              widget=forms.TextInput(attrs={'placeholder': 'Dropoff', 'class': 'dropoff-textbox'}))
    # date = forms.CharField(max_length = 10, label = 'Date', widget = forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    date = forms.DateField(widget=DatePickerInput(format='YYYY-MM-DD'))
    time = forms.DateField(widget=TimePickerInput())

class userLogin(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'login-email', 'placeholder': 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'login-password',
            'placeholder': 'Password',
        }
    ))


class userSignup(forms.Form):
    firstname = forms.CharField(widget = forms.TextInput(attrs = {'class': 'signup-firstname', 'placeholder':'Enter your Firstname'}))
    lastname = forms.CharField(widget = forms.TextInput(attrs = {'class': 'signup-lastname', 'placeholder':'Enter your Lastname'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'signup-email', 'placeholder': 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'signup-password',
            'placeholder': 'Password',
            'type': 'password'
        }
    ))



