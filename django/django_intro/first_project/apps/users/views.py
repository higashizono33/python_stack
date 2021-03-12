from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# def index(request):
#     return HttpResponse("placeholder for users to display users info")

def register(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def login(request):
    return HttpResponse("placeholder for users to log in")

# def new(request):
#     return HttpResponse("placeholder for users to log in")

def users(request):
    return HttpResponse("placeholder to later display all the list of users")

# def show(request, number):
#     return HttpResponse("placeholder to display blog number: {}".format(number))

# def edit(request, number):
#     return HttpResponse("placeholder to edit blog {}".format(number))

# def destroy(request, number):
#     return redirect("/")