from django.shortcuts import render, redirect
from django.contrib import messages

from login_app.models import Users
from .models import Messages, Comments
# Create your views here.
def index(request):
    try: 
        user = Users.objects.get(id=request.session['userid'])
        messages = Messages.objects.all()
        # comments = Messages.objects.all()
        context = {
            'user': user,
            'posted_messages': messages,
        }
        return render(request, 'wall.html', context)
    except:
        return redirect('/')

def post_message(request):
    if request.method == 'POST':
        Messages.objects.create(message=request.POST['message'], user=Users.objects.get(id=request.session['userid']))
    return redirect('/wall')

def delete_message(request):
    if request.method == 'POST':
        errors = Messages.objects.delete_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            to_delete = Messages.objects.get(id=request.POST['message_id'])
            if request.session['userid'] == int(request.POST['user_id']):
                to_delete.delete()
    return redirect('/wall')

def post_comment(request):
    if request.method == 'POST':
        print(request.POST['message_id'])
        Comments.objects.create(comment=request.POST['comment'], message=Messages.objects.get(id=request.POST['message_id']),
        user=Users.objects.get(id=request.session['userid']))
    return redirect('/wall')

def logout(request):
    request.session.flush()
    return redirect('/')
