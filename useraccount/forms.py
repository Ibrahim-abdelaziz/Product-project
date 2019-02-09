from django import forms
from django.contrib.auth.models import User
from .models import Profile
from . import models


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email' , 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic']

