""" Form object related to the Place model.It will be used to create
 input field that will map to the columns in the database. """

from django import forms
from .models import Place
import django.core.validators

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name','visited') #model fields


class DateInput(forms.DateInput):
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes','date_visited', 'photo')
        widgets = {
            'date_visited':DateInput(format='%m-%d-%Y')
        }