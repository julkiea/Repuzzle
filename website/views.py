from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Home page
def home(request):
    return render(request, 'home.html', {})

# Register user 
def register_user(request):
    return render(request, 'register_user.html', {})

# Log in user 
def login_user(request):

    # Check if user is logging in 
    if request.method == "POST":
        
        # Get username and password
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user 
        user = authenticate(request, username = username, password = password)

        # Check if authenticating is succes 
        if user is not None:

            # Log in 
            login(request, user)

            # Message about logging in 
            messages.success(request, "Zalogowano poprawnie...")

        else: 
            messages.success(request, "Wystąpił błąd w trakcie logowania... Spróbuj ponownie!")
            return redirect('login_user')
        
    # If not logging in 
    else:
        return render(request, 'login_user.html')
            
    return render(request, 'login_user.html', {})

# Logo out user
def logout_user(request):
    return redirect('home')
