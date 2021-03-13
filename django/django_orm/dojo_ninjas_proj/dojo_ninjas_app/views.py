from django.shortcuts import render, HttpResponse, redirect
from .models import Dojos, Ninjas

# Create your views here.
def index(request):
    context = {
        "all_the_dojos": Dojos.objects.all(),
        "all_the_ninjas": Ninjas.objects.all(),
    }
    return render(request, "index.html", context)

def new_dojo(request):
    if request.method == 'POST':
        if request.POST.get('dojo_name') and request.POST.get('dojo_city') and request.POST.get('dojo_state'):
            dojo = Dojos()
            dojo.name = request.POST.get('dojo_name')
            dojo.city = request.POST.get('dojo_city')
            dojo.state = request.POST.get('dojo_state')
            dojo.save()
            return render(request, "create.html")
        else:
            return HttpResponse('your entry did not process')
    else:
        redirect('/')

def new_ninja(request):
    if request.method == 'POST':
        if request.POST.get('ninja_first_name') and request.POST.get('ninja_last_name') and request.POST.get('ninja_dojo_name'):
            ninja = Ninjas()
            ninja_dojoId = Dojos.objects.get(name=request.POST.get('ninja_dojo_name')).id
            ninja.dojo_id = ninja_dojoId

            ninja.first_name = request.POST.get('ninja_first_name')
            ninja.last_name = request.POST.get('ninja_last_name')
            ninja.save()
            return render(request, "create.html")
        else:
            return HttpResponse('your entry did not process')
    else:
        redirect('/')

def delete(request, location):
    delete_dojo = Dojos.objects.get(name=location)
    delete_ninjas = Ninjas.objects.filter(dojo=delete_dojo)
    delete_dojo.delete()
    delete_ninjas.delete()
    return redirect('/')