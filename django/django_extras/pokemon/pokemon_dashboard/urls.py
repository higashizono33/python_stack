from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('favorite/add/<int:pokemon_id>', views.add_favorite),
    path('favorite/<int:user_id>', views.show_favorite, name='favorite'),
    path('favorite/delete/<int:pk>', views.delete_favorite),
]