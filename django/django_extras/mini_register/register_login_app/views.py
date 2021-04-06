from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from .forms import *
from .models import User
# Create your views here.
def index(request):
    r_form = RegistrationForm()
    l_form = LoginForm()
    context = {
        'r_form': r_form,
        'l_form': l_form,
    }
    return render(request, 'form.html', context)

def success(request):
    print(request.session['userid'])
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user': user,
    }
    return render(request, 'home.html', context)

def register(request):
    # Confirm that the HTTP verb was a POST
    if request.method == "POST":
        # Bind the POST data to an instance of our RegisterForm
        bound_form = RegistrationForm(request.POST)
        # Now test that bound_form using built-in methods!
        # *************************
        print(bound_form.is_valid()) # True or False, based on the validations that were set!
        print(bound_form.errors) # Any errors in this form as a dictionary
        # *************************
        if bound_form.is_valid():
            bound_form.password = make_password(bound_form.cleaned_data['password'])
            user = bound_form.save()
            print(user.id)
            request.session['userid'] = user.id
            return redirect('success')
        else:
            context = {
                'r_form': bound_form,
                'l_form': LoginForm(),
            }
            return render(request, 'form.html', context)

def login(request):
    if request.method == "POST":
        bound_form = LoginForm(request.POST)
        user = User.objects.filter(email=request.POST['email']).first()
        if user is not None and user.password == request.POST['password']:
            request.session['userid'] = user.id
            return redirect('success')
        else:
            context = {
                'l_form': bound_form,
                'r_form': RegistrationForm(),
            }
            return render(request, 'form.html', context)