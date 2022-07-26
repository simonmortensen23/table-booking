'''
Structure for the booking form, based on bookingmodel
'''

import datetime
from django import forms
from django.forms import TextInput, SelectDateWidget


from feedme.models import Booking


class BookingForm(forms.ModelForm):
    """
    Control booking creation here.
    """

    class Meta:
        """
        Meta Class to construct booking form from the model.
        """
        model = Booking
        fields = [
            'customer', 'people', 'phone_number', 'booking_date',
            'booking_time']

        widgets = {
            'customer': TextInput(),
            'booking_date': SelectDateWidget(
                years=(datetime.date.today().year, datetime.date.today().year
                       + 1)),
            'booking_time': forms.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        """
        Add class, required field
        to third field.
        """
        super().__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs['required'] = 'required'
        self.fields['people'].widget.attrs['required'] = 'required'
        self.fields['phone_number'].widget.attrs['required'] = 'required'
        self.fields['booking_date'].widget.attrs['required'] = 'required'
        self.fields['booking_time'].widget.attrs['required'] = 'required'
