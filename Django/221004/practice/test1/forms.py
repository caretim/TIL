from django import forms
from .models import tests


class test1Form(forms.ModelForm):
    class Meta:
        model = tests
        fields = "__all__"
