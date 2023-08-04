from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms

class signup_form(UserCreationForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={
        "class": "input-field"
    }))
    class Meta:
        model = Account
        fields = ['email', 'username', 'cpf', 'password1', 'password2', 'data_nascimento']
        
