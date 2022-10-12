from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(label="이메일")

        model = User
        fields = ("username", "password1", "password2", "email")
