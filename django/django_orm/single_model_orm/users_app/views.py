# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Users

def index(request):
    users =  Users.objects.all()
    return render(request, 'index.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            age = request.POST['age'],
        )
    return redirect('/')