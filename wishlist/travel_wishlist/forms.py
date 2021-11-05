""" Form object related to the Place model.It will be used to create
 input field that will map to the columns in the database. """

from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name','visited') #model fields