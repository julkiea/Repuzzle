from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms


# User creation form 

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Adres e-mail: '}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Imię: '}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nazwisko: '}))

    class Meta():
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'input-field'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'input-field'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdź hasło'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'