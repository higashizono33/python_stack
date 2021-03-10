from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    request.session['counter'] = 0
    context = {
        'counter': request.session['counter'],
    }
    return render(request, 'index.html', context)

def random_word(request):
    if request.method == 'POST':
        request.session['word'] = get_random_string(length=14)
        request.session['counter'] += 1
    return redirect('/result')

def reset(request):
    request.session['word'] = ''
    request.session['counter'] = 0
    return redirect('/random_word')

def result(request):
    context = {
        'counter': request.session['counter'],
        'random_word': request.session['word'],
    }
    return render(request, 'index.html', context)
