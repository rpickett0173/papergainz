from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'Home.html')
def signUp(request):
    return render(request, 'Sign Up.html')
    #return render(request, 'Sign UP.html')
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