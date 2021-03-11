from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main),
    path('process_money/<location>', views.process_money),
    path('reset', views.reset),
    # path('process_money/cave', views.process_money_cave),
    # path('process_money/house', views.process_money_house),
    # path('process_money/casino', views.process_money_casino),
]