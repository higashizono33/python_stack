from django.db import models
from django.core import validators

class Post(models.Model):
    post = models.TextField(max_length=150, validators=[validators.MinLengthValidator(15, message='Post should be at least 15 letters long')])
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
