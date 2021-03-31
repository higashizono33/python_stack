from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User
# Create your views here.
def index(request):
    return render(request, 'base.html')

def show_register(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        User.objects.create(
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            password = pw_hash,
            user_level = 9,
        )

    return redirect('/signin')

def show_signIn(request):
    return render(request, 'signin.html')

def signIn(request):
    user = User.objects.filter(email=request.POST['email'])
    errors = User.objects.signin_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/signin')
    else:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            if logged_user.user_level == 9:
                return redirect('/dashboard/admin')
            else:
                return redirect('/dashboard')
        else:
            messages.error(request, 'Password doesn\'t match with the email')
            return redirect('/signin')