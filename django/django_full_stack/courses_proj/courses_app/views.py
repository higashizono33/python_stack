from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Course, Description, Comment

# Create your views here.
def index(request):
    return render(request, 'index.html', {'all_course': Course.objects.all()})

def create(request):
    name_error = Course.objects.basic_validator(request.POST)
    desc_error = Description.objects.basic_validator(request.POST)
    errors = {**name_error, **desc_error}
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        if request.method == 'POST':
            new_course = Course.objects.create(name=request.POST['name'])
            new_description = Description.objects.create(course=new_course, content=request.POST['description'])
            new_course.save()
            new_description.save()
        return render(request, 'index.html', {'all_course': Course.objects.all()})

def confirmToDelete(request, course_id):
    return render(request, 'delete.html', {'delete_course': Course.objects.get(id=course_id)})

def delete(request, course_id):
    delete_course = Course.objects.get(id=course_id)
    delete_course.delete()
    return redirect('/')

def comment(request, course_id):
    context = {
        'comment_course': Course.objects.get(id=course_id),
        'comments': Comment.objects.filter(course_id=course_id),
    }
    return render(request, 'comment.html', context)

def addComment(request, course_id):
    if request.method == 'POST':
        new_comment = Comment.objects.create(course_id=course_id, comment=request.POST['comment'])
        new_comment.save()
    return redirect(f'/courses/comment/{course_id}')
