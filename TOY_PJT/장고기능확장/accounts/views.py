from django.shortcuts import render, redirect
from .foms import signupForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as as_login, logout as as_logout

# Create your views here.


def accounts_index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = signupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = signupForms()
    context = {"form": form}

    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    contetx = {"form": form}
    return render(request, "accounts/login.html", contetx)


def logout(request):
    as_logout(request)
    return redirect("articles:index")
