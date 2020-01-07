from django.contrib import admin
from django.urls import path

from stocks.views import create_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_post, name="create")
]