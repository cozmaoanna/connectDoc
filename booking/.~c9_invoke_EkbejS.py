from django import forms
from .models import Booking
import datetime

    doctor = Booking.doctor

    doctorText = forms.CharField()
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


