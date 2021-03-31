from django.shortcuts import render, redirect

from apps.login_app.models import User
# Create your views here.
def dashboard(request):
    all_users = User.objects.all()
    logged_user = User.objects.get(id=request.session['userid'])
    context = {
        'users': all_users,
        'user': logged_user,
    }

    return render(request, 'general.html', context)

def dashboard_admin(request):
    all_users = User.objects.all()
    logged_user = User.objects.get(id=request.session['userid'])
    context = {
        'users': all_users,
        'user': logged_user,
    }

    return render(request, 'admin.html', context)
