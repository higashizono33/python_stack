# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')

    errors = User.objects.user_validator(request.POST) 
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        User.objects.create(
            name = name,
            alias = alias,
            email = email,
            password = pw_hash,
        )
        messages.success(request, "You are successfully registered")
        return redirect('/')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    
    errors = User.objects.login_validator(request.POST) 
    user = User.objects.filter(email=request.POST['email'])
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:    
        logged_user = user[0] 
        request.session['userid'] = logged_user.id
    return redirect("/books")

def home(request):
    user = User.objects.get(id=request.session['userid'])
    # don't know how to make distinct on reviews in below
    recent_reviews = Review.objects.all().order_by('-updated_at')[:3]
    other_reviews = Review.objects.all().order_by('-updated_at')[3:]
    context = {
        'user': user,
        'recent_reviews': recent_reviews,
        'other_reviews': other_reviews,
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def add_book(request):
    recent_authors = Author.objects.all().order_by('-updated_at')[:5]
    return render(request, 'add_book.html', {'authors': recent_authors})

def create_book(request):
    if request.method == 'GET':
        return redirect('/')

    errors = Book.objects.book_validator(request.POST) 
    errors_review = Review.objects.review_validator(request.POST)
    errors.update(errors_review)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/add')
    else:
        title = request.POST['title']
        author = request.POST['author']
        user = User.objects.get(id=request.session['userid'])
        review = request.POST['review']
        rating = request.POST['rating']
        
        Author.objects.create(
            name = author
        )
        author_toBook = Author.objects.filter(name=author)

        Book.objects.create(
            title = title,
            author = author_toBook[0],
            uploaded_by = user,
        )
        book = Book.objects.get(title=title)
        Review.objects.create(
            review = review,
            rating = rating,
            reviewed_by = user,
            reviewed_to = book
        )

        return redirect(f'/books/{book.id}')

def show_book(request, book_id):
    user = User.objects.get(id=request.session['userid'])
    this_book = Book.objects.get(id=book_id)
    book_reviews = Review.objects.filter(reviewed_to=this_book).order_by('-updated_at')[:3]

    context = {
        'user': user,
        'book': this_book,
        'book_reviews': book_reviews,
    }
    return render(request, 'show_book.html', context)

def add_review(request, book_id):
    if request.method == 'GET':
        return redirect('/')

    errors = Review.objects.review_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')
    else:
        user = User.objects.get(id=request.session['userid'])
        book = Book.objects.get(id=book_id)
        review = request.POST['review']
        rating = request.POST['rating']
        
        Review.objects.create(
            review = review,
            rating = rating,
            reviewed_by = user,
            reviewed_to = book
        )

        return redirect(f'/books/{book_id}')

def delete_review(request, review_id):
        to_delete = Review.objects.get(id=review_id)
        book_id = to_delete.reviewed_to.id
        to_delete.delete()
        return redirect(f'/books/{book_id}')

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    posted_reviews = Review.objects.filter(reviewed_by=user).order_by('-updated_at')
    posted_total = Review.objects.filter(reviewed_by=user).count()

    context = {
        'user': user,
        'reviews': posted_reviews,
        'total': posted_total,
    }
    return render(request, 'show_user.html', context)