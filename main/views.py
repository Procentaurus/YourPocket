from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange
import pytz


from main.decorators import *
from .forms import *
from .models import *
from .functions import *
from .filters import *

def home(request):

    context = {}
    return render(request, 'main/home.html', context)

def profileDataVisualisation(request):

    period = None
    try:
        period = request.GET.get('period')
    except:
        pass

    all_expenses = request.user.customer.expense_set.all()
    all_incomes = request.user.customer.income_set.all()

    if period is not None:
        start, end, option = None, datetime.date.today(), None
        if period == "all":
            start = datetime.datetime.max.replace(tzinfo=pytz.UTC)
            
            for expense in all_expenses:
                if (expense.date_created).replace(tzinfo=pytz.UTC) < start:
                    start = expense.date_created

            for income in all_incomes:
                if (income.date_created).replace(tzinfo=pytz.UTC) < start:
                    start = income.date_created
            start = start.date()
            option = "all"

        elif period == "last":
            end = end - relativedelta(months=1)
            lastDay = monthrange(end.year, end.month)
            end = datetime.date(end.year, end.month, lastDay[1])
            lastDay = monthrange(end.year, end.month)
            start = datetime.date(end.year, end.month, 1)
            option = "last"

        elif period == "last3":
            start = end - relativedelta(months=2)
            start = datetime.date(start.year, start.month, 1)
            option = "last3"

        elif period == "lasty":
            start = datetime.date(end.year - 1, end.month + 1, end.day)
            option = "lasty"

        elif period == "this":
            start = datetime.date(end.year, end.month, 1)
            option = "this"

        else:
            start = datetime.date.min
            option = ""

        data = {
            'total_incomes' : sumOfData(all_incomes.values('value', 'date_created'), start, end),
            'total_expenses' : sumOfData(all_expenses.values('value', 'date_created'), start, end),
            'expenses_by_categories' : createPercentage(all_expenses.values('value', 'category', 'date_created'), start, end),
            'incomes_by_categories' : createPercentage(all_incomes.values('value', 'category', 'date_created'), start, end),
            'incomes_by_period': createPeriodData(all_incomes.values('value', 'date_created'), start, end, option),
            'expenses_by_period': createPeriodData(all_expenses.values('value', 'date_created'), start, end, option),
        }
        return JsonResponse(data, DjangoJSONEncoder, True)

@login_required(login_url='login')
@differentUser
def profile(request, pk):
    active = None
    if request.GET.get('active') is None:
        active = 'income'
    else:
        active = request.GET.get('active')

    user = User.objects.get(id=pk)
    customer = user.customer

    expense_form = CreateExpenseForm()
    income_form = CreateIncomeForm()

    all_expenses = customer.expense_set.all()
    all_incomes = customer.income_set.all()

    #   expense filter
    exp_filter = ExpenseFilter(request.GET, queryset=all_expenses)
    all_expenses_filtered = exp_filter.qs

    #   income filter
    inc_filter = IncomeFilter(request.GET, queryset=all_incomes)
    all_incomes_filtered = inc_filter.qs

    #   pagination for expenses
    expenses_paginator = Paginator(all_expenses_filtered,20)
    expenses_page_number = request.GET.get('exp_page')
    if expenses_page_number is None:
        expenses_page_number = 1
    expenses_page_obj = expenses_paginator.get_page(expenses_page_number)
    expenses_number_of_pages = expenses_paginator.num_pages

    #   pagination for incomes
    income_paginator = Paginator(all_incomes_filtered,20)
    incomes_page_number = request.GET.get('inc_page')
    if incomes_page_number is None:
        incomes_page_number = 1
    incomes_page_obj = income_paginator.get_page(incomes_page_number)
    incomes_number_of_pages = income_paginator.num_pages

    context = {
        'customer': customer,
        'expenses_page': expenses_page_obj,
        'incomes_page': incomes_page_obj,

        'num_inc_pages': incomes_number_of_pages,
        'num_exp_pages': expenses_number_of_pages,

        'expense_form':expense_form,
        'income_form':income_form,

        'exp_filter': exp_filter,
        'inc_filter': inc_filter,

        'active': active,
    }
    return render(request, 'main/profile.html', context)

@login_required(login_url='login')
@differentUser
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

@unauthenticatedUser
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

@unauthenticatedUser
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


    context = {'page': page, 'form': form}
    return render(request, 'main/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def addIncome(request):
    if request.method =='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        value = request.POST.get('value')

        income = Income.objects.create(
            name = name,
            category = category,
            value = value,
            customer = request.user.customer,
        )
        return redirect('confirm', income.id, 'income')
    else:
        return redirect('home')

def addExpense(request):
    if request.method =='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        value = request.POST.get('value')
        user = request.user

        expense = Expense.objects.create(
            name = name,
            category = category,
            value = value,
            customer = user.customer,
        )
        return redirect('confirm', expense.id, 'expense')
    else:
        return redirect('home')

@login_required(login_url='login')
def confirm(request, pk, type):
    if type == 'expense':
        object = Expense.objects.get(id=pk)
    else:
        object = Income.objects.get(id=pk)
    
    context = {
        'object': object,
        'type': type,
    }
    return render(request, 'main/confirm.html', context)

@login_required(login_url='login')
def deleteObject(request, type, pk):
    responce =  redirect('profile', request.user.id)
    responce['Location'] += f'?active={type}'
    try:
        object = Expense.objects.get(id=pk) if type == 'expense' else Income.objects.get(id=pk)
    except:
        return responce

    if request.method == 'POST':
        object.delete()
        return responce

    context = {
        'object': object,
        'type': type,
    }
    return render(request, 'main/delete.html', context)

@login_required(login_url='login')
def editObject(request, type, pk):
    form, object = None, None
    if type == 'expense':
        object = Expense.objects.get(id=pk)
        form = CreateExpenseForm(instance=object)
    else:
        object = Income.objects.get(id=pk)
        form = CreateIncomeForm(instance=object)
    
    if request.method =='POST':
        form = CreateExpenseForm(request.POST, instance=object) if type == 'expense' else CreateIncomeForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            responce =  redirect('profile', request.user.id)
            responce['Location'] += f'?active={type}'
            return responce
 
    context = {
        'form': form,
        'type': type,
        'object': object,
    }
    return render(request, 'main/edit.html', context)

def error404_view(request, exception):
    context = {
        'error': '404',
    }
    return render(request, 'main/error.html', context, status=404)

def error500_view(request):
    context = {
        'error': '500',
    }
    return render(request, 'main/error.html', context, status=500)

@login_required(login_url='login')
def contactSupport(request):
    if request.method =='POST':
        messageBody = request.POST.get('message_body')
        chosenCase = request.POST.get('chosenCase') if request.POST.get('chosenCase') is not None else "Others"
        email = request.POST.get('email')
        emailMessage = "Email from: "+ email +"\n\n"+ messageBody
        try:
            send_mail(
                chosenCase,
                emailMessage,
                None,
                ['michalski.44@wp.pl'],
                fail_silently=False,
            )
            messages.info(request, 'Your message was sent successfully.')
        except:
            messages.error(request, 'An error occured during sending mail, try later..')
            return render(request, 'main/contact.html')

        return redirect('home')
        
    context = {
        "source": "contactSupport"
    }
    return render(request, 'main/contact.html', context)

def contactInfo(request):
    context = {
        "source": "contactInfo"
    }
    return render(request, 'main/contact.html', context)