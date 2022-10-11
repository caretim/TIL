from django.shortcuts import render, redirect
from .models import User

from django.contrib.auth import authenticate, login
from .forms import HCreateForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = HCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("accounts:index")
    else:
        form = HCreateForm()
        context = {"form": form}
    return render(request, "users/signup.html", context)


def index(request):
    users = User.objects.all()

    context = {"users": users}

    return render(request, "users/index.html", context)


def joinlist(request):
    users = User.objects.all()

    context = {"users": users}

    return render(request, "users/joinlist.html", context)


def profil(reuqest, pk):
    user = User.objects.get(pk=pk)

    context = {
        "user": user,
    }
    return render(reuqest, "users/profil.html", context)
