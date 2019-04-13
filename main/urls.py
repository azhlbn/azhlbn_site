from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('fonts', fonts, name='fonts'),
    path('tg-logo', tg_logo, name='tg_logo'),
    path('shop', shop, name='shop'),
]
