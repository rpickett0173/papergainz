from django.urls import path
from . import views
#home
urlpatterns = [
    path('Home.html', views.home, name='home'),
    path('Sign.html', views.signUp, name='signUp')
]