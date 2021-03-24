from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Books
from login_app.models import Users
# Create your views here.
def index(request):
    user =  Users.objects.get(id=request.session['userid'])
    books =  Books.objects.all().order_by('-updated_at')
    like_books = user.liked_books.all()
    context = {
        'user': user,
        'books': books,
        'like_books': like_books,
    }
    return render(request, 'base.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def create_book(request):
    errors = Books.objects.books_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        user = Users.objects.get(id=request.session['userid'])
        Books.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=user)
    
    return redirect('/books')

def edit_book(request, book_id):
    user = Users.objects.get(id=request.session['userid'])
    this_book = Books.objects.get(id=book_id)
    like_users = this_book.users_who_like.all()
    context = {
        'user': user,
        'book': this_book,
        'like_users': like_users,
    }
    return render(request, 'edit.html', context)

def update_book(request, book_id):
    errors = Books.objects.books_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        update_book = Books.objects.get(id=book_id)
        update_book.title = request.POST['title']
        update_book.description = request.POST['description']
        update_book.save()
    
    return redirect('/books')

def delete_book(request, book_id):
    delete_book = Books.objects.get(id=book_id)
    delete_book.delete()

    return redirect('/books')

def add_favorite(request, book_id):
    favorite_book = Books.objects.get(id=book_id)
    favorite_book.users_who_like.add(request.session['userid'])
    
    return redirect('/books')

def remove_favorite(request, book_id):
    favorite_book = Books.objects.get(id=book_id)
    favorite_book.users_who_like.remove(request.session['userid'])
    
    return redirect('/books')