from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.allShows),
    path('shows/new', views.addShows),
    path('shows/new/create', views.createShows),
    path('shows/<int:show_id>', views.detailShows),
    path('shows/<int:show_id>/edit', views.editShows),
    path('shows/<int:show_id>/update', views.updateShows),
    path('shows/<int:show_id>/destroy', views.destroyShows),
    path('shows/ajax/validate_title', views.validate_title, name='validate_title'),
]
