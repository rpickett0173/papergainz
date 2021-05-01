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
    path("", hello.views.index, name="hello"),
    # path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('Home.html', views.home),
    path('Sign Up.html', views.signUp),
    path('Login.html', views.login_view),
    path('CSGO.html', views.CSGO),
    path('DOTA.html', views.DOTA),
    path('Player Rankings.html', views.player_rankings),
    path('League.html', views.League),
    path('Baseball.html', views.Baseball),
    path('Hockey.html', views.Hockey),
    path('Basketball.html', views.Basketball),
    path('eSports.html', views.eSports),
    path('My Bets.html', views.myBets),
    path('Sports.html', views.sports),
    path('Rewards.html', views.rewards),
    path('My Profile.html', views.myProfile),
    path('Inventory.html', views.inventory),
    path('test.html', views.test),
    path('test_mybets.html', views.test_mybets, name='test_mybets'),
    path('bet_button.html', views.bet_button),


]

# urltestpatterns = [
    # path('admin/', admin.site.urls),
    # path('Home.html', views.home),
    # path('Sign Up.html', views.signUp),
    # path('CSGO.html', views.CSGO),
    # path('eSports.html', views.eSports),
    # path('My Bets.html', views.myBets),
    # path('Sports.html', views.sports),
    # path('Rewards.html', views.rewards),
    # path('My Profile.html', views.myProfile),
    # path('Inventory.html', views.inventory)
#
# ]
