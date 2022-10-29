from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path("index/", views.accounts_index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/accounts_detail/", views.accounts_detail, name="accounts_detail"),
    path("accounts_list", views.accounts_list, name="accounts_list"),
    path("<int:user_pk>", views.follow, name="follow"),
]
