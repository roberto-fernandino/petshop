from django import forms
from .models import Tosa, Banho

class TosaForm(forms.ModelForm):
    pet = forms.CharField(max_length=30,
                          min_length=3,
                          widget=forms.TextInput(attrs={
                              'class': "input-field",
                              'name': 'pet',
                              'required': True,
                              "maxlength": "30",
                              "minlength": '3',
                          }))
    
    data = forms.DateTimeField(input_formats=['%H:%M %d/%m/%Y'], widget=forms.DateTimeInput(attrs={
        "type": 'datetime-local',
        'name': 'data',
        'required': True,
        'class': 'date-input-field',
    }))
    class Meta:
        model = Tosa
        fields = ['pet', 'data']


class BanhoForm(forms.ModelForm):
    pet = forms.CharField(max_length=30,
                          min_length=3,
                          widget=forms.TextInput(attrs={
                              'class': 'input-field',
                              'required': True,
                              'name': "pet",
                              'maxlength': "30",
                              "min length":'3',
                          }))
    data = forms.DateTimeField(input_formats=['%H %M %d/%m/%Y'],
                               widget=forms.DateTimeInput(attrs={
                                   "type": 'datetime-local',
                                   "name": "data",
                                   "required": True,
                                   'class': 'date-input-field',
                               }))
    class Meta:
        model = Banho
        fields = ['pet', 'data']