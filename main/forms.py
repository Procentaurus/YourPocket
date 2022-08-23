from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password..'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password..'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username..',
                }),
            'email': forms.EmailInput(attrs={
                        'class':'form-control',
                        'placeholder':'Email..',
                        'required':'True'
                }),
        }

class CreateCustomerForm(ModelForm):
    avatar = forms.ImageField(required=False)
    class Meta:
        model = Customer
        fields =  '__all__'
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username..',
                }),
            'email': forms.EmailInput(attrs={
                        'class':'form-control',
                        'placeholder':'Email..',
                }),
            'phone': forms.NumberInput(attrs={
                        'class':'form-control',
                        'placeholder':'123 456 789',
                }),
            'date_of_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class':'form-control',
                }),
        }