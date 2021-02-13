from django.contrib import admin

from django.urls import path
from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetaulView.as_view(), name='detail'),


]
