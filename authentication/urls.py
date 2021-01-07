from django.urls import path
#from . import views
from authentication.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', registerPage, name='register'),

    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]




