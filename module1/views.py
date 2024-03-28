import random
import string

from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello1(request):
    return HttpResponse("<center>Welcome to MNC Homepage</center>")

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'print_to_console.html',a1)

def randomcall(request):
    return render(request,'randomotpgenerator.html')

def randomlogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1={'ran1':ran1}
    return render(request,'randomotpgenerator.html',a1)

def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
from .forms import IntegerDateForm, PieChartForm


def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})


def myregisterpage1(request):
    return render(request, 'myregisterpage.html')




from .models import *
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Neha.objects.filter(email=email).exists():
            return HttpResponse(" Email already registered.Choose a differenet email")
        Neha.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request, 'myregisterpage.html')

def myfeedbackform1(request):
    return render(request, 'feedbackform.html')

from django.core.mail import send_mail
def feedbackformfunction(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        suggestions = request.POST.get('suggestions')
        if contactus.objects.filter(email=email).exists():
            return HttpResponse("Feedback already submitted.")
        contactus.objects.create(name=name,email=email,suggestions=suggestions)
        tosend = suggestions + '------------------This is just a copy of your comments'
        send_mail(
            'Thank you for Contacting YOGIs travel treasures Tourism and Management',
            tosend,
            '2200030532cseh@gmail.com',
            [email],
            fail_silently='False'

        )
        return redirect('newhomepage')
    return render(request,'feedbackform.html')
def getPieChart(request):
    return render(request, 'PieChart.html')



import matplotlib.pyplot as plt
import numpy as np

def PieChart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'PieChart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'PieChart.html', {'form': form})

def Car(request):
    return render(request,'Car.html')


import requests

def weatherpagecall(request):
    return render(request,'weatherinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'e501f7d63df269821b1db3312772a948'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherinput.html', {'error_message': error_message})

from django.shortcuts import render

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.checks import messages
def login(request):
    return render(request,'Login.html')
def login1(request):
    if request.method=='POST':
        username=request.POST.get['username']
        pass1=request.POST.get['password']
        Yogi=auth.authenticate(username=username,password=pass1)
        if Yogi is not None:
            auth.login(request,Yogi)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'Login.html')
    else:
        return render(request,'Login.html')

def signup(request):
    return render(request,'signup.html')
def signup1(request):
 if request.method=="POST":
    username=request.POST.get['username']
    pass1=request.POST.get['password']
    pass2=request.POST.get['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'Login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'newhomepage.html')






