from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LeadList.as_view(), name='index'),
    path('from_date', filter_from_date, name='filter_from_date'),
    path('date', filter_date, name='filter_date'),
    path('name', filter_name, name='filter_name'),
]