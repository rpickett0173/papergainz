from django.shortcuts import render
from django.http import HttpResponse
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
def CSGO(request):
    return render(request, 'CSGO.html')
def eSports(request):
    return render(request, 'eSports.html')
def myBets(request):
    return render(request, 'MyBets.html')
def sports(request):
    return render(request, 'Sports.html')
def rewards(request):
    return render(request, 'Rewards.html')
def myProfile(request):
    return render(request, 'MyProfile.html')
def inventory(request):
    return render(request, 'Inventory.html')
