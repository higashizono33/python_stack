from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books/new', views.book_register),
    path('books/<int:book_id>/', views.book_details),
    path('books/<int:book_id>/author', views.add_author),
    path('authors', views.index_authors),
    path('authors/new', views.author_register),
    path('authors/<int:author_id>', views.author_details),
    path('authors/<int:author_id>/book', views.add_book),
]