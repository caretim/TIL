from django.contrib import admin
from django.urls import path
from .views import *
from users import views  # views 모든 함수를 가져온다.
from django.contrib.auth import views as auth_views


app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # 코드 추가하기
    path("signup/", views.signup, name="signup"),
]
