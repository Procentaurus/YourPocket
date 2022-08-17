from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import *

def home(request):

    context = {}
    return render(request, 'main/home.html', context)

def profile(request):

    context = {}
    return render(request, 'main/profile.html', context)
