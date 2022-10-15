from django.shortcuts import render, redirect
from .forms import NewB, OldB, PCForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    update_session_auth_hash,
    logout as as_logout,
    login as as_login,
)
from .models import Huser
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(reuqest):
    all_user = Huser.objects.all()

    context = {"all_user": all_user}

    return render(reuqest, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = NewB(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = NewB()
        context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
        return redirect("accounts:index")

    else:
        form = AuthenticationForm()
        context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    as_logout(request)

    return redirect("accounts:index")


def profil(reqeust, pk):
    user_info = Huser.objects.get(pk=pk)

    context = {"user_info": user_info}

    return render(reqeust, "accounts/profil.html", context)


@login_required
def profil_update(request):
    if request.method == "POST":
        form = OldB(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profil", request.user.pk)
    else:
        form = OldB(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/profil_update.html", context)


@login_required
def profil_password(request):
    if request.method == "POST":
        form = PCForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            as_logout(request)
            return redirect("accounts:profil_update")
    else:
        form = PCForm(request.user)
    context = {"form": form}
    return render(request, "accounts/profil_password.html", context)


def delete_info(request):
    request.user.delete()
    as_logout(request)
    return redirect("accounts:index")
