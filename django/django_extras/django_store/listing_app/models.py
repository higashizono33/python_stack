from django.db import models
from django.core import validators

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, validators=[validators.MinLengthValidator(8, 'Please enter at least 8 charactors')])
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[validators.MinValueValidator(1, 'Please set more than $0')])
    description = models.TextField(validators=[validators.MinLengthValidator(50, 'Please enter at least 50 charactors')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
