from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import *

def home(request):

    context = {}
    return render(request, 'main/home.html', context)

def profile(request):

    context = {}
    return render(request, 'main/profile.html', context)

def loginPage(request):
    page='login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login or password incorrect')


    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def registerPage(request):
    page='register'
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registartion')


    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')