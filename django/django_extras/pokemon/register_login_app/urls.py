from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('secret/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('login/', views.LoginView.as_view(), name='login'),
]