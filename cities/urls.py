from django.contrib import admin

from django.urls import path
from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('list', CityListView.as_view(), name='list'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),

]
