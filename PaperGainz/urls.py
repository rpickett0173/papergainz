"""PaperGainz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Paper Gainz
from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home.html', views.home),
    path('Sign Up.html', views.signUp),
    path('CSGO.html', views.CSGO),
    path('eSports.html', views.eSports),
    path('My Bets.html', views.myBets),
    path('Sports.html', views.sports),
    path('Rewards.html', views.rewards),
    path('My Profile.html', views.myProfile),
    path('Inventory.html', views.inventory)

]