from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# User creation anb authentication ...
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Flash message ...
from django.contrib import messages


# User Creation, Authorization and Authentication ....
def registerPage(request, template_name='register.html'):
    if request.user.is_authenticated:
        return redirect('user-profile')

    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login.')
            return redirect('login')

    context = {'form': form}
    return render(request, template_name, context)


def loginPage(request, template_name='customLogin.html'):
    if request.user.is_authenticated:
        return redirect('user-profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-profile')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, template_name, context)


def logoutUser(request):
    logout(request)
    return redirect('home')

# def login(request, template_name='users/login.html'):
#     return render(request, template_name)
