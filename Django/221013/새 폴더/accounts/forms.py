from dataclasses import fields
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model


class NewB(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class OldB(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
        #


class PCForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"
