from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.home),
    path('books/add', views.add_book),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/add_review', views.add_review),
    path('books/<int:review_id>/delete_review', views.delete_review),
    path('users/<int:user_id>', views.show_user),
]