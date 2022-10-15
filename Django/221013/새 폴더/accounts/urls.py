from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("profil/<int:pk>", views.profil, name="profil"),
    path("profil_update/", views.profil_update, name="profil_update"),
    path("profil_password/", views.profil_password, name="profil_password"),
    path("delete_info/", views.delete_info, name="delete_info"),
]
