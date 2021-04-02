from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('courses/delete/<int:course_id>', views.confirmToDelete),
    path('courses/delete/<int:course_id>/execute', views.delete),
    path('courses/comment/<int:course_id>', views.comment),
    path('courses/comment/<int:course_id>/execute', views.addComment),
]