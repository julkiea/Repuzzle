from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import Puzzle, Category, UserProfile
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

# Create a UserInfoForm

class UserInfoForm(forms.ModelForm):

    phone = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Numer telefonu',
            'aria-label': 'Numer telefonu'
        })
    )

    address1 = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Adres zamieszkania 1',
            'aria-label': 'Adres zamieszkania 1'
        })
    )

    address2 = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Adres zamieszkania 2',
            'aria-label': 'Adres zamieszkania 2'
        })
    )

    city = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Miasto',
            'aria-label': 'Miasto'
        })
    )

    zipcode = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Kod pocztowy',
            'aria-label': 'Kod pocztowy'
        })
    )

    country = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Kraj',
            'aria-label': 'Kraj'
        })
    )

    bank_account_code = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Numer konta bankowego',
            'aria-label': 'Numer konta bankowego'
        })
    )


    class Meta():
        model = UserProfile
        fields = ("phone", "address1", "address2", "city", "zipcode",  )


# Create a Update User Password Form

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'password',
            'placeholder': 'Nowe hasło',
            'aria_label': 'Nowe hasło 1'
        })
    )

    new_password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'password',
            'placeholder': 'Potwierdź nowe hasło',
            'aria_label': 'Nowe hasło 2'
        })
    )

    class Meta():
        model = User
        fields = ("new_password1", "new_password2")

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

# Create a PuzzleForm

class AddPuzzleForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ('Nowy', 'Nowy'),
        ('Bardzo dobry', 'Bardzo dobry'),
        ('Dobry', 'Dobry'),
        ('Średni', 'Średni'),
        ('Zły', 'Zły'),
    ]
    
    name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Nazwa',
            'aria-label': 'Nazwa puzzli'
        })
    )
    
    description = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Opis',
            'aria-label': 'Opis puzzli'
        })
    )
    
    brand = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Producent',
            'aria-label': 'Producent puzzli'
        })
    )
    
    price = forms.DecimalField(
        label="",
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'input',
            'type': 'number',
            'placeholder': 'Cena',
            'step': '0.01',
            'min': '0',
            'aria-label': 'Cena puzzli'
        })
    )

    condition = forms.ChoiceField(
        label="",
        required=False,
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'condition-input',
            'aria-label': 'Stan puzzli'
        })
    )
    
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'custom-checkbox-group custom-checkbox',
            'aria-label': 'Kategoria puzzli'
        }),
    )

    image = forms.FileField(
        label="",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'image-input',
            'aria-label': 'Obrazek puzzli'
        })
    )

    class Meta:
        model = Puzzle
        fields = ('name', 'description', 'brand', 'category', 'price', 'condition', 'image')

    def __init__(self, *args, **kwargs):
        super(AddPuzzleForm, self).__init__(*args, **kwargs)

