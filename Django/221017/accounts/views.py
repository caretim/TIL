from django.shortcuts import render, redirect
from .models import Huser

# Create your views here.
from django.contrib.auth import login as as_login, logout as as_logout
from django.contrib.auth.forms import AuthenticationForm


def index(request):

    return render(request, "accounts/index.html")


def signup(request):

    return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
        context = {"form": form}

    return render(request, "accounts/login.html", context)


def logout(request):
    as_logout(request)
    return redirect("articles:index")
