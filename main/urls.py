from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('fonts', fonts, name='fonts'),
    path('tg-logo', tg_logo, name='tg_logo'),
    path('shop', shop, name='shop'),
    path('btw-dates', btw_dates, name='btw-dates'),
    path('operations-with-matrix', operations_with_matrix, name='operations_with_matrix'),
]
