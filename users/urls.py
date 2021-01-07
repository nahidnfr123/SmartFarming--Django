from django.urls import path
#from . import views
from users.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', profile, name='user-profile'),
]




