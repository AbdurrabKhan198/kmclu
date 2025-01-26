from django import forms
from .models import WebApp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class KMCLUForm(forms.ModelForm):
    class Meta:
        model = WebApp
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')