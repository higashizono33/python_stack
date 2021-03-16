from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.allShows),
    path('shows/new', views.view_addShows),
    path('shows/new/create', views.addShows),
    path('shows/<int:show_id>', views.detailShows),
    path('shows/<int:show_id>/edit', views.view_editShows),
    path('shows/edit/<int:show_id>', views.editShows),
    path('shows/<int:show_id>/destroy', views.destroyShows),
]
