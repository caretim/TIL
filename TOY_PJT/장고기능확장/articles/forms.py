from tkinter.tix import Form
from django import forms
from .models import article


class MakeArticle(forms.ModelForm):
    class Meta:
        model = article
        fields = "__all__"
