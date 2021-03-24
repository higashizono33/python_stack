from django.shortcuts import render, redirect
from django.contrib import messages
# from django.http import JsonResponse
import bcrypt


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
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)
        Users.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=hashed_pw,
            # birthday=request.POST['birthday'] 
        )
        return redirect('/')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = Users.objects.get(email=request.POST['email'])
        request.session['userid'] = user.id
        return redirect('/books')

# def success_login(request):
#     try: 
#         user = Users.objects.get(id=request.session['userid'])
#         return render(request, 'user.html', {'user_name': user.first_name})
#     except:
#         return redirect('/')

# def logout(request):
#     request.session.flush()
#     return redirect('/')

# def validate_title(request):
#     title = request.GET.get('title', None)
#     data = {
#         'is_taken': Shows.objects.filter(title__iexact=title).exists()
#     }
#     return JsonResponse(data)