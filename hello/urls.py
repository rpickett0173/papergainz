from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#home
urlpatterns = [
    path('Home.html', views.hello, name='hello'),
    path('Sign.html', views.signUp, name='signUp')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
