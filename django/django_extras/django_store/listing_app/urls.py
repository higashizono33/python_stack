from django.urls import path
from .views import *

urlpatterns = [
    path('products', Products.as_view(), name="products"),
    path(r'^products/(?P<id>\d+)$', EditProduct.as_view(), name="editing"),
    path(r'^products/(?P<id>\d+)/delete$', delete, name="deleting"),
]