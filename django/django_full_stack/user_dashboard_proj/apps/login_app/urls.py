from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.show_register),
    path('register/user', views.register),
    path('signin', views.show_signIn),
    path('signin/user', views.signIn),
]