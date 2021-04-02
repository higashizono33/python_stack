from django.shortcuts import render, redirect
from django.db.models import Q

from ..login_app.models import Users
from ..courses_app.models import Course
from .models import Dashboard

# Create your views here.
def index(request):
    all_course = Course.objects.all()
    my_dict = {}
    for course in all_course:
        my_dict[course.id] = [course.name, Dashboard.objects.filter(course__name=course.name).count()]
    # print(my_dict)
    context = {
        'users': Users.objects.all(),
        'courses': all_course,
        'my_dict': my_dict,
    }
    return render(request, 'table.html', context)

def add_to_course(request):
    user = Users.objects.get(id=request.POST['user'])
    course = Course.objects.get(id=request.POST['course'])
    Dashboard.objects.create(
        user = user,
        course = course,
    )
    return redirect('/')