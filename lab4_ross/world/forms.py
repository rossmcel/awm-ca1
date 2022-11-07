import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class AddMarkerForm(forms.Form):
    name = forms.CharField(max_length=30)
    lat = forms.FloatField()
    lng = forms.FloatField()

    class Meta:
        model = models.WorldBorder
        fields = ('name', 'lat', 'lng')

    # def clean_name(self):
    #     data = self.cleaned_data['name']

    #     # # Check if a date is not in the past.
    #     # if data < datetime.date.today():
    #     #     raise ValidationError(_('Invalid date - renewal in past'))

    #     # # Check if a date is in the allowed range (+4 weeks from today).
    #     # if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #     #     raise ValidationError(
    #     #         _('Invalid date - renewal more than 4 weeks ahead'))

    #     # Remember to always return the cleaned data.
    #     return data
