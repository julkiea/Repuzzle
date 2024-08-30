from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm, AddPuzzleForm, UserInfoForm, UpdatePasswordForm
from .models import Puzzle, UserProfile
from django.core.paginator import Paginator

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
        if request.method == 'POST':
            form = AddPuzzleForm(request.POST, request.FILES)

            if form.is_valid():
                puzzle = form.save(commit=False)
                puzzle.owner = request.user
                puzzle.save()

                messages.success(request, "Puzzle zostały dodane pomyślnie!")
                return redirect('home')
            else:
                messages.error(request, "Wystąpił błąd podczas dodawania puzzli... Spróbuj ponownie")
                return render(request, 'add_puzzle.html', {'form': form})
        else:
            form = AddPuzzleForm()

        return render(request, 'add_puzzle.html', {'form': form})
    
    else:
        messages.warning(request, "Musisz być zalogowany, aby sprzedawać puzzle. Zaloguj się i spróbuj ponownie.")
        return redirect('home')
    
def puzzle_list(request):
    puzzles  = Puzzle.objects.all().order_by('added_at')
    paginator = Paginator(puzzles, 9) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(f"Page Number: {page_number}")
    print(f"Page Object: {page_obj}")
    return render(request, 'puzzle_list.html', {'page_obj': page_obj})


def puzzle(request, pk):
    try:
        puzzle = get_object_or_404(Puzzle, id=pk)
        return render(request, "puzzle.html", {'puzzle': puzzle})
    except Puzzle.DoesNotExist:
        messages.error(request, "Te puzzle nie istnieją.")
        return redirect('home')
    

def update_info(request):
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user__id = request.user.id)

        form = UserInfoForm(request.POST or None, instance = user)
        if form.is_valid():
            form.save()

            messages.success(request, "Twój profil został zaktualizowany pomyślnie...")
            return redirect('home')
        return render(request, "update_info.html", {'form':form})
    else:
        messages.warning(request, "Aby zaktualizować profil, musisz być zalogowany...")
        return redirect('home')
    
def update_password(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        if request.method == "POST":
            form = UpdatePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Twoje hasło zostało zaktualizowane pomyślnie!")
                login(request, user)
                return redirect('home')
            else:

                messages.error(request, "W trakcie zmiany hasła wystąpił błąd... Sprawdź, czy oba wprowadzane hasła są jednakowe i spróbuj ponownie!")
                return redirect('update_password')

        else:
            form = UpdatePasswordForm(user)
            return render(request, "update_password.html", {"form": form})
    else:
        messages.success(request, "Aby zaktualizować hasło, musisz być zalogowany...")
        return redirect('home')