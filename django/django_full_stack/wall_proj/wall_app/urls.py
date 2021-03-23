from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('post-message', views.post_message),
    path('post-comment', views.post_comment),
    path('delete-message', views.delete_message),
    path('logout', views.logout),
]