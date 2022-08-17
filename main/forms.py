from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['avatar']
