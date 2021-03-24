from django.urls import path     
from . import views
urlpatterns = [
    # books
    path('', views.index),
    path('logout', views.logout),
    path('create', views.create_book),
    path('<int:book_id>', views.edit_book),
    path('<int:book_id>/update', views.update_book),
    path('<int:book_id>/delete', views.delete_book),
    path('<int:book_id>/add_favorite', views.add_favorite),
    path('<int:book_id>/remove_favorite', views.remove_favorite),
]
