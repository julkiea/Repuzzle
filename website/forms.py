from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms


# User creation form 

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={
        'class': 'input',
        'type': 'text',
        'placeholder': 'Nazwa użytkownika'
        }))
    
    first_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={
        'class': 'input', 
        'type': 'text',
        'placeholder': 'Imię'
        }))

    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={
        'class': 'input', 
        'type': 'text',
        'placeholder': 'Nazwisko'
        }))

    email = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={
        'class': 'input',
        'type': 'email',
        'placeholder': 'Adres e-mail'
        }))
    
    password1 = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={
        'class': 'input',
        'type': 'password',
        'placeholder': 'Hasło'
        }))

    password2 = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={
        'class': 'input',
        'type': 'password',
        'placeholder': 'Potwierdź hasło'
        }))


    usable_password = None

    class Meta():
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)