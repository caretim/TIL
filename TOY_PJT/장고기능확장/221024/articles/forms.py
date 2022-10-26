from tkinter.tix import Form
from django import forms
from .models import article, Comment


class MakeArticle(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            "title",
            "content",
            "movie_name",
            "grade",
            "img",
        ]


class MakeComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
