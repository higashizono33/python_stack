from django.urls import path
from .views import *

urlpatterns = [
    path('', Calculator.as_view(), name='index')
]