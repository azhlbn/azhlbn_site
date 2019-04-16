from django.urls import path
from .views import *

urlpatterns = [
    path('', placestogo, name='placestogo'),
    path('<str:slug>/', place_details, name='place_details'),
]