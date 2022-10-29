from django.shortcuts import render, redirect, get_object_or_404
from .foms import signupForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as as_login, logout as as_logout, get_user_model
from .models import Huser
from articles.models import article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


def accounts_index(request):
    return render(request, "accounts/index.html/")


def signup(request):
    if request.method == "POST":
        form = signupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = signupForms()
    context = {"form": form}

    return render(request, "accounts/signup.html/", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            as_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    contetx = {"form": form}
    return render(request, "accounts/login.html/", contetx)


def logout(request):
    as_logout(request)
    return redirect("articles:index")


@login_required
def accounts_detail(request, pk):
    user_info = Huser.objects.get(pk=pk)
    user_article = user_info.article_set.all()

    context = {
        "user_info": user_info,
        "user_article": user_article,
    }

    return render(request, "accounts/accounts_detail.html", context)


@login_required
def accounts_list(request):
    user_info = Huser.objects.all()
    context = {
        "user_info": user_info,
    }

    return render(request, "accounts/accounts_list.html", context)


@login_required
def follow(request, user_pk):
    pick_user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user != pick_user:
        if request.user in pick_user.followings.all():
            pick_user.followings.remove(request.user)
        else:
            pick_user.followings.add(request.user)
    return redirect("accounts:accounts_detail", user_pk)
