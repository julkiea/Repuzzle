from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm

# Home page
def home(request):
    return render(request, 'home.html', {})

# Register user 
def register_user(request):

    # Check if signing in
    if request.method == 'POST':

        # Create instance of SignUpForm
        form = RegisterUserForm(request.POST)

                # Check if form is valid
        if form.is_valid():

            # Create a user 
            form.save()
            
            # Get username and password from cleaned data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:

                login(request, user)
                
                # If authentication is successful
                messages.success(request, "Zarejestrowano pomyślnie...")

                return redirect('home')

            else:
                messages.error(request, "Rejestracja nie powiodła się... Sprawdź poprawność formularza i spróbuj ponownie!")
                return redirect('register_user')
        #else:
            #messages.error(request, "Rejestracja nie powiodła się... Sprawdź poprawność formularza i spróbuj ponownie!")
            #return redirect('register_user')
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})

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
            messages.success(request, "Zalogowano pomyślnie...")
            return redirect('home')

        else: 
            messages.error(request, "Wystąpił błąd w trakcie logowania... Spróbuj ponownie!")
            return redirect('login_user')
        
    # If not logging in 
    else:
        return render(request, 'login_user.html')


# Log out user
def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie...")
    return redirect('home')


# Add a puzzle

def add_puzzle(request):
    if request.user.is_authenticated:
        return render(request, 'add_puzzle.html', {})
    else:
        messages.warning(request, "Musisz być zalogowany, aby sprzedawać puzzle. Zaloguj się i spróbuj ponownie...")
        return redirect('home')