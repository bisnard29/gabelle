from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'stocks'
urlpatterns = [
    path('', views.create_post, name='create'),
   # path('#entree', views.create_post, name='create'),
]