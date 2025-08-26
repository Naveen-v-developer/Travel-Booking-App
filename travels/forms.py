from django import forms
from .models import TravelOption

class TravelFilterForm(forms.Form):
    type = forms.ChoiceField(choices=[('', 'All')] + TravelOption.TRAVEL_TYPE_CHOICES, required=False)
    source = forms.CharField(max_length=100, required=False)
    destination = forms.CharField(max_length=100, required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
