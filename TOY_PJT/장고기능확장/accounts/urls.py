from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path("index/", views.accounts_index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
