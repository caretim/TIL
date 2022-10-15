from dataclasses import field
from pyexpat import model
from .models import Review, Movie
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "movie_name", "grade"]


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
