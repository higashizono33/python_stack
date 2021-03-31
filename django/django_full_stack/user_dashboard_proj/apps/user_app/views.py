from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from apps.login_app.models import User
from .models import *
# Create your views here.
def show_addUser(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user': user,
    }
    return render(request, 'add_user.html', context)

def addUser(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        User.objects.create(
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            password = pw_hash,
            user_level = 3,
        )

    return redirect('/dashboard/admin')

def show_editUser(request):
    user = User.objects.get(id=request.session['userid'])
    
    context = {
        'user': user,
    }
    return render(request, 'edit.html', context)

def admin_editUser(request, userId):
    logged_user = User.objects.get(id=request.session['userid'])
    user = User.objects.get(id=userId)
    
    context = {
        'user': user,
        'logged_user': logged_user,
    }
    return render(request, 'admin_edit.html', context)

def editUser_info(request):
    user = User.objects.get(id=request.POST['id'])
    errors = User.objects.edit_info_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/users/edit/{user.id}')
    else:
        logged_user = User.objects.get(id=request.session['userid'])
        if logged_user.user_level == 9:
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.user_level = request.POST['user_level']
            user.save()
            return redirect('/dashboard/admin')
        else:
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return redirect('/dashboard')

def editUser_pass(request):
    user = User.objects.get(id=request.POST['id'])
    errors = User.objects.edit_pass_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/users/edit/{user.id}')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        user.password = pw_hash
        user.save()
        logged_user = User.objects.get(id=request.session['userid'])
        if logged_user.user_level == 9:
            return redirect('/dashboard/admin')
        else:
            return redirect('/dashboard')

def editUser_desc(request):
    user = User.objects.get(id=request.POST['id'])
    user.description = request.POST['description']    
    user.save()
    logged_user = User.objects.get(id=request.session['userid'])
    if logged_user.user_level == 9:
        return redirect('/dashboard/admin')
    else:
        return redirect('/dashboard')

def admin_deleteUser(request, userId):
    user_delete = User.objects.get(id=userId)
    user_delete.delete()
    return redirect('/dashboard/admin')

def showUser(request, userId):
    user = User.objects.get(id=userId)
    logged_user = User.objects.get(id=request.session['userid'])
    messages = Message.objects.filter(message_to=user)
    # comments = Comment.objects.all()
    context = {
        'user': user,
        'logged_user': logged_user,
        'messages': messages,
        # 'comments': comments,
    }
    return render(request, 'show_user.html', context)

def post_message(request, userId):
    poster = User.objects.get(id=request.session['userid'])
    receiver = User.objects.get(id=userId)
    Message.objects.create(
        message = request.POST['message'],
        message_from = poster,
        message_to = receiver,
    )
    
    return redirect(f'/users/show/{userId}')

def post_comment(request, messageId):
    poster = User.objects.get(id=request.session['userid'])
    receiver_id = request.POST['id']
    message = Message.objects.get(id=messageId)
    Comment.objects.create(
        comment = request.POST['comment'],
        comment_from = poster,
        comment_to = message,
    )
    
    return redirect(f'/users/show/{receiver_id}')

def logoff(request):
    request.session.flush()
    return redirect('/')