from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import *
from .functions import deleteFile

def home(request):

    context = {}
    return render(request, 'main/home.html', context)

def profile(request,pk):

    customer = (User.objects.get(id=pk)).customer

    context = {'customer': customer}
    return render(request, 'main/profile.html', context)

def settings(request,pk):
    customer = (User.objects.get(id=pk)).customer
    form = CreateCustomerForm(instance=customer)

    isImage = request.POST.get('avatar-clear')
    picture = customer.avatar

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            if isImage =='on':
                customer.avatar = '/model.png'
                customer.save()
                if not deleteFile(picture):
                    messages.error(request, "You can't delete default picture")
            if customer.avatar != picture:
                deleteFile(picture)

            messages.info(request, "Profile updated successfully")
            
    context = {'form': form}
    return render(request, 'main/settings.html', context)


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login or password incorrect')

    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def registerPage(request):
    page='register'
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')


    context = {'page': page, 'form':form}
    return render(request, 'main/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')