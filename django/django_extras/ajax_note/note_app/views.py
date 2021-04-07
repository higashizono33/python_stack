from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {
                'form': form, 
                'posts': Post.objects.order_by('-created_at')[:3],
            }
            return render(request, 'home.html', context)
    else:
        form = PostForm()
        context = {
            'form': form, 
            'posts': Post.objects.order_by('-created_at')[:3],
        }
        return render(request, 'home.html', context)
