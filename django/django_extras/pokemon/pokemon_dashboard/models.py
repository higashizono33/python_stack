from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class MyPokemon(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pokemon_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
