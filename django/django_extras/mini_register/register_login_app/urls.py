from django.urls import path     
# from django.conf.urls import url     
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('success', views.success, name="success"),
]