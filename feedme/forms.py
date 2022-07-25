import datetime

from django.forms import ModelForm, Select, ValidationError, TextInput, SelectDateWidget

from feedme.models import Booking


class BookingForm(ModelForm):
    """
    Control booking creation here.
    """


    class Meta:
        model = Booking
        fields = ['costumer', 'table', 'people', 'booking_date_time_start', 'booking_date_time_end']

        widgets = {
            'costumer': TextInput(),
            'date': SelectDateWidget(years=(datetime.date.today().year, datetime.date.today().year + 1))
        }

    def __init__(self, *args, **kwargs):
        """
        Add class, required field and DateTime picker
        to third field.
        """
        super().__init__(*args, **kwargs)
        self.fields['booking_date_time_start'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['booking_date_time_start'].widget = DateTimeField()
        self.fields['booking_date_time_start'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['required'] = 'required'