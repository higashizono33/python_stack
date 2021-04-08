from django.db import models
from django.core import validators

class Note(models.Model):
    title = models.CharField(max_length=30,validators=[validators.MinLengthValidator(2, message='Title should be at least 2 letters long')])
    content = models.TextField(max_length=150, validators=[validators.MinLengthValidator(15, message='Content should be at least 15 letters long')])
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
