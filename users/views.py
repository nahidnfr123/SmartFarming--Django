from django.shortcuts import render, redirect
from django.http import HttpResponse

# User creation anb authentication ...
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Flash message ...
from django.contrib import messages


@login_required(login_url='login')
def profile(request, template_name='profile.html'):
    return render(request, template_name)

