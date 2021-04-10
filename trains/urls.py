from django.contrib import admin

from django.urls import path
from trains.views import *
urlpatterns = [
    path('', home, name='home'),
    path('list', TrainListView.as_view(), name='list'),
    path('detail/<int:pk_Train>/', TrainDetailView.as_view(), name='detail'),
    path('create/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk_Train>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk_Train>/', TrainDeleteView.as_view(), name='delete'),

]
