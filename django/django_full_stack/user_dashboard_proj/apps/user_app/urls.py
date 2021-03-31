from django.urls import path     
from . import views
urlpatterns = [
    path('new', views.show_addUser),
    path('new/register', views.addUser),
    path('edit', views.show_editUser),
    path('edit/<int:userId>', views.admin_editUser),
    path('edit/update/info', views.editUser_info),
    path('edit/update/pass', views.editUser_pass),
    path('edit/update/desc', views.editUser_desc),
    path('remove/<int:userId>', views.admin_deleteUser),
    path('show/<int:userId>', views.showUser),
    path('<int:userId>/message', views.post_message),
    path('<int:messageId>/comment', views.post_comment),
    path('logoff', views.logoff),
]