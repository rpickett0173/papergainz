from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Users
from .models import Greeting

import requests
import os

# Create your views here.
def index(request):
    return render(request, 'Home.html')



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def home(request):
    return render(request, 'Home.html')
def signUp(request):
    return render(request, 'Sign Up.html')
def myBets(request):
    return render(request, 'myBets.html')
def rewards(request):
    return render(request, 'rewards.html')
def myProfile(request):
    return render(request, 'myProfile.html')
def inventory(request):
    return render(request, 'inventory.html')
#ESPORTS
def eSports(request):
    return render(request, 'eSports.html')
def CSGO(request):
    return render(request, 'CSGO.html')
def CSGO_1(request):
    return render(request, 'CSGO_1.html')
def DOTA(request):
    return render(request, 'DOTA.html')
def DOTA_1(request):
    return render(request, 'DOTA_1.html')
def league(request):
    return render(request, 'league.html')
def league_1(request):
    return render(request, 'league_1.html')
#SPORTS
def sports(request):
    return render(request, 'sports.html')
def Baseball(request):
    return render(request, 'Baseball.html')
def Baseball_1(request):
    return render(request, 'Baseball_1.html')
def Basketball(request):
    return render(request, 'Basketball.html')
def Basketball_1(request):
    return render(request, 'Basketball_1.html')
def Football(request):
    return render(request, 'Football.html')
def Football_1(request):
    return render(request, 'Football_1.html')


def test(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            temp=Users(username=username,password=raw_password)
            temp.save()

            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('Home.html')
    else:
        print("failed")
        form = UserCreationForm()
    return render(request, 'test.html', {'form': form})
