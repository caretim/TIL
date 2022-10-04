# URL설정은 APP단위로 해준다.
from django.urls import path, include
from . import views


app_name = "test1"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
