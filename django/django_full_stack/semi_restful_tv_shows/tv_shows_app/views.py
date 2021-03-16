from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

# Create your views here.
def index(request):
    return redirect('/shows')

def allShows(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, 'all_shows.html', context)

def view_addShows(request):
    return render(request, 'add_shows.html')

def addShows(request):
    Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'],
    description=request.POST['description'])
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

def view_editShows(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    context = {
        'id': this_show.id,
        'title': this_show.title,
        'network': this_show.network,
        'release_date': this_show.release_date,
        'description': this_show.description,
    }
    return render(request, 'edit_shows.html', context)

def editShows(request, show_id):
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