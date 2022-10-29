from dataclasses import field
from socket import fromshare
from django import forms
from .models import Article, Comment


class A_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "content",
        ]


class C_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
