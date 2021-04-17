from django.urls import path
from . import views
#sign UP

urlpatterns = [
    path('home/Sign Up.html', views.signUp, name='signUp')
]