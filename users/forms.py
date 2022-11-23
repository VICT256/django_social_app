import email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone',]