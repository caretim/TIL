from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .form import JoinForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:main')
    else:
        form = JoinForm()
    context ={
        'form': form
    }
    return render(request,"accounts/signup.html",context)


def login(request):
    if request.method == 'POST':
        form =AuthenticationForm(request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("articles:main")
    else:
        form = AuthenticationForm()
        context={'form':form}

    return render(request,"accounts/login.html",context)