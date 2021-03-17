from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import Shows
# Create your views here.
def index(request):
    return redirect('/shows')

def allShows(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, 'all_shows.html', context)

def addShows(request):
    return render(request, 'add_shows.html')

def createShows(request):
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'],
        description=request.POST['description'])
        # messages.success(request, "Blog successfully updated")
        return redirect('/shows')

def detailShows(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    context = {
        'id': this_show.id,
        'title': this_show.title,
        'network': this_show.network,
        'release_date': this_show.release_date,
        'description': this_show.description,
        'updated_at': this_show.updated_at,
    }
    return render(request, 'detail_shows.html', context)

def editShows(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    context = {
        'id': this_show.id,
        'title': this_show.title,
        'network': this_show.network,
        'release_date': this_show.release_date,
        'description': this_show.description,
    }
    return render(request, 'edit_shows.html', context)

def updateShows(request, show_id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        edit_show = Shows.objects.get(id=show_id)
        edit_show.title = request.POST['title']
        edit_show.network = request.POST['network']
        edit_show.release_date = request.POST['release_date']
        edit_show.description = request.POST['description']
        edit_show.save()
        return redirect(f'/shows/{show_id}')

def destroyShows(request, show_id):
    destroy_show = Shows.objects.get(id=show_id)
    destroy_show.delete()
    return redirect('/shows')

def validate_title(request):
    title = request.GET.get('title', None)
    data = {
        'is_taken': Shows.objects.filter(title__iexact=title).exists()
    }
    return JsonResponse(data)