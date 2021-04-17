from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#signUp

def signUp(request):
    return render(request, 'Sign Up.html')