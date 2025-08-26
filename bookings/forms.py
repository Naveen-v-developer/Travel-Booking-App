from django import forms
from .models import Booking
from travels.models import TravelOption

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def __init__(self, *args, **kwargs):
        self.travel_option = kwargs.pop('travel_option', None)
        super().__init__(*args, **kwargs)

    def clean_number_of_seats(self):
        seats = self.cleaned_data['number_of_seats']
        if self.travel_option and seats > self.travel_option.available_seats:
            raise forms.ValidationError('Cannot book more seats than available.')
        if seats < 1:
            raise forms.ValidationError('Must book at least 1 seat.')
        return seats
