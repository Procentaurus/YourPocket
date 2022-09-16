from distutils.command.upload import upload
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
    # class MyImageField(forms.ImageField):
    #     @property
    #     def url(self):
    #         return "static/images/user_images/{name}".format(name=self.name)
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

class CreateExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['customer']
        widgets = {
            'name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Name of the expence..',
                }),
            'category': forms.Select(attrs={
                        'class':'form-control',
                }),
            'value': forms.NumberInput(attrs={
                        'class':'form-control',
                        'placeholder':'Value of the expence..',
                }),
        }

class CreateIncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
        exclude = ['customer']
        widgets = {
            'name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Name of the income..',
                }),
            'category': forms.Select(attrs={
                        'class':'form-control',
                }),
            'value': forms.NumberInput(attrs={
                        'class':'form-control',
                        'placeholder':'Value of the income..',
                }),
        }