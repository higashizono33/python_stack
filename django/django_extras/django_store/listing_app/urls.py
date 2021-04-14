from django.urls import path
from .views import *

urlpatterns = [
    path('products', Products.as_view(), name="products"),
    path('products/<int:id>', EditProduct.as_view(), name="editing"),
    path('products/<int:id>/delete', delete, name="deleting"),
]