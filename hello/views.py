from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    return render(request, "Rewards.html")
    return render(request, "Sports.html")
>>>>>>> parent of b2556ab (t)
=======
    return render(request, "Rewards.html")
    return render(request, "Sports.html")
>>>>>>> parent of 43cf074 (t)
=======
    return render(request, "Rewards.html")
    return render(request, "Sports.html")
>>>>>>> parent of 43cf074 (t)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
