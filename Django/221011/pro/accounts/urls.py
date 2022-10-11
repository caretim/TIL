from django.urls import path
from django.contrib.auth import login
from . import views
from django.contrib.auth import views as auth_views


app_name = "accounts"


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("joinlist/", views.joinlist, name="joinlist"),
    path("profil/<int:pk>", views.profil, name="profil"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
