from django import forms
from .models import chicken



class testForm(forms.ModelForm):
    class Meta:
        model = chicken
        fields = '__all__'