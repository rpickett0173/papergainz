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
    path('admin/', admin.site.urls),
    path('Home.html', views.home),
    path('Sign Up.html', views.signUp),
    path('CSGO.html', views.CSGO),
    path('eSports.html', views.eSports),
    path('My Bets.html', views.myBets),
    path('Sports.html', views.sports),
    path('Rewards.html', views.rewards),
    path('My Profile.html', views.myProfile),
    path('Inventory.html', views.inventory),
    path('test.html', views.test)
]

# urlpatterns = [
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
