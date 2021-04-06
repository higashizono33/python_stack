from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .forms import UserCreateForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
            }    
    else:
        form = UserCreateForm()
        context = {
            'form': form,
        }
    return render(request, 'registration/signup.html', context)

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


