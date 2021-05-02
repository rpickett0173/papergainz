from django.urls import path, include
from django.contrib import admin
import hello.views
from hello import views
admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.home, name='Paper Gainz'),
    path('Home.html', views.home, name='Paper Gainz'),
    path('Login.html', views.login_view, name='Login'),
    path('Sign Up.html', views.signUp, name='Sign Up'),
    path('My Profile.html', views.myProfile, name='My Profile'),
    path('My Bets.html', views.myBets, name='My Bet History'),
    path('FAQ.html', views.FAQ, name='Frequently Asked Questions'),

    path('eSports.html', views.eSports, name='eSports'),
    path('CSGO.html', views.CSGO, name='CS:GO'),
    path('league.html', views.league, name='League of Legends'),
    path('DOTA.html', views.DOTA, name='DOTA 2'),
    path('Player Rankings.html', views.player_rankings, name='Dota Pro Player Rankings'),

    path('Sports.html', views.sports, name='Sports'),
    path('Baseball.html', views.Baseball, name='MBA'),
    path('Basketball.html', views.Basketball, name='NBA'),
    path('Hockey.html', views.Hockey, name='NHL'),

    path('test_gamepage.html', views.test_gamepage, name='Testing Game Page'),
    path('test_mybets.html', views.test_mybets, name='Testing Bet History'),
    path('test_signup.html', views.test_signup, name='Testing Signup')
]
