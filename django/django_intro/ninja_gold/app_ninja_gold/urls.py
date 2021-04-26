from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main),
    path('process_money/<location>', views.process_money),
    path('reset', views.reset),
]