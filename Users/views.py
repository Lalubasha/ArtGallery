from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth_login(request, user)  # Log in the user after registration
                messages.success(request, 'Account created successfully. You are now logged in.')
                return redirect('/')  # Redirect to main page
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('/')  # Redirect to main page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
def profile(request):
    return render(request, "profile.html")