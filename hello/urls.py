from django.urls import path
from . import views
#home
urlpatterns = [
    path('Home.html', views.hello, name='hello'),
    path('Sign.html', views.signUp, name='signUp')
]
