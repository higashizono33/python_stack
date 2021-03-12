from django.urls import path
from . import views
from apps.app_one import views as views_app_one

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views_app_one.index),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.users),
    # path('<int:number>', views.show),
    # path('<int:number>/edit', views.edit),
    # path('<int:number>/delete', views.destroy),
]