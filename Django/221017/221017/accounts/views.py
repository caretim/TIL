from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request, "accounts/index.html")


def signup(request):

    return render(request, "accounts/signup.html")
