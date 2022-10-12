from django.shortcuts import render, redirect
from .forms import HuserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as as_logout, login as as_login
from .models import Huser

# Create your views here.


def index(request):
    all_date = Huser.objects.all()
    context = {"all_date": all_date}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = HuserCreateForm(request.POST)
        form.is_valid()
        form.save()
        return redirect("accounts:login")
    else:
        form = HuserCreateForm()
        context = {"form": form}

        return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = form = AuthenticationForm()
    context = {"form": form}

    return render(request, "accounts/login.html", context)


def logout(request):
    as_logout(request)

    return redirect("accounts:index")


def profil(reuqest, pk):
    user = Huser.objects.get(pk=pk)

    context = {
        "user": user,
    }
    return render(reuqest, "accounts/profil.html", context)
