from django.shortcuts import render, redirect
from .models import MyPokemon
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'home.html')

def add_favorite(request, pokemon_id):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user_id'])
        MyPokemon.objects.create(
            user_id = user,
            pokemon_id = pokemon_id,
        )
        print('success')
    return redirect('home')

def show_favorite(request, user_id):
    pokemons = MyPokemon.objects.filter(user_id=int(user_id))
    context = {
        'pokemons': pokemons,
    }
    return render(request, 'favorite.html', context)

def delete_favorite(request, pk):
    if request.method == 'POST':
        pokemon_delete = MyPokemon.objects.get(id=int(pk))
        pokemon_delete.delete()
        user_id = request.POST['user_id']
        print('delete')
    return redirect('favorite', user_id)