from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email", 'password1', 'password2']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']