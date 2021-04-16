from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('index_2', views.index_2, name="index_2"),
	path('make_data', views.make_data, name="make_data"),
]