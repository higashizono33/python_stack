from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def home(request):
    # u_form = UpdateForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {
                'form': form,
                # 'u_form': u_form, 
                'notes': Note.objects.order_by('-id')[:3],
            }
            return render(request, 'home.html', context)
    else:
        form = NoteForm()
        context = {
            'form': form, 
            # 'u_form': u_form, 
            'notes': Note.objects.order_by('-id')[:3],
        }
        return render(request, 'home.html', context)

def update(request):
    if request.method == 'POST':
        note = Note.objects.get(id=request.POST['id'])
        note.title = request.POST['title'] 
        note.content = request.POST['content']
        note.save(force_update=True)
    return redirect('home')

def delete(request):
    if request.method == 'POST':
        note = Note.objects.get(id=request.POST['id'])
        note.delete()
    return redirect('home')