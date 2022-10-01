from django.urls import path
from . import views


app_name = "todos"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<todo_pk>", views.delete, name="delete"),
    path("edit/<todo_pk>", views.edit, name="edit"),
    path("detail/<detail_pk>", views.detail, name="detail"),
]
