from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from django.contrib.auth.decorators import login_required

from .models import Users
# Create your views here.
def index(request):
    request.session.flush()
    return render(request, 'login.html')

def create(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)
        Users.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=hashed_pw,
            birthday=request.POST['birthday'] 
        )
    return redirect('/login')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        user = Users.objects.get(email=request.POST['email'])
        request.session['userid'] = user.id
        return redirect('/login/success')
    return redirect("/login")

# tried to see how login_required works
@login_required(login_url='/')
def success_login(request):
    return render(request, 'user.html')
    
    # try: 
    #     user = Users.objects.get(id=request.session['userid'])
    #     return render(request, 'user.html', {'user_name': user.first_name})
    # except:
    #     return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/login')