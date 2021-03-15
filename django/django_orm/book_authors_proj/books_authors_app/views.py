from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Book, Author
# show all of the data from a table
def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "book.html", context)

def index_authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "author.html", context)

def book_register(request):
    if request.method == 'POST':
        new_title = request.POST['book_title'] 
        new_desc = request.POST['book_desc']
        Book.objects.create(title=new_title, desc=new_desc)
    else:
        return HttpResponse('registration was failed')
    
    return redirect('/')

def book_details(request, book_id):
    this_book = Book.objects.get(id=book_id)
    all_authors = Author.objects.all()
    this_book_authors = this_book.authors.all()
    excluded_authors = all_authors.exclude(id__in=[o.id for o in this_book_authors])
    context = {
        "book_title": this_book.title,
        "book_id": this_book.id,
        "book_desc": this_book.desc,
        "book_authors": this_book.authors.all(),
        "excluded_authors": excluded_authors,
    }
    return render(request, "detail.html", context)

def add_author(request, book_id):
    this_book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        selected_id = request.POST['authorsToAdd'] 
        this_book.authors.add(selected_id)
    else:
        return HttpResponse('You are failed to add..')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def author_register(request):
    if request.method == 'POST':
        new_firstName = request.POST['author_firstName'] 
        new_lastName = request.POST['author_lastName']
        new_note = request.POST['author_note']
        Author.objects.create(first_name=new_firstName, last_name=new_lastName, note=new_note)
    else:
        return HttpResponse('registration was failed')
    
    return redirect('/authors')

def author_details(request, author_id):
    this_author = Author.objects.get(id=author_id)
    all_books = Book.objects.all()
    author_books = this_author.books.all()
    excluded_books = all_books.exclude(id__in=[o.id for o in author_books])
    context = {
        "author_first_name": this_author.first_name,
        "author_last_name": this_author.last_name,
        "author_id": this_author.id,
        "author_note": this_author.note,
        "author_books": author_books,
        "all_books": all_books,
        "excluded_books": excluded_books,
    }
    return render(request, "author_detail.html", context)

def add_book(request, author_id):
    this_author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        selected_id = request.POST['booksToAdd'] 
        this_author.books.add(selected_id)
    else:
        return HttpResponse('You are failed to add..')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

