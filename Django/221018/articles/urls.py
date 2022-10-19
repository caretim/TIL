from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/delete_comment/", views.delete_comment, name="delete_comment"),
    path("<int:pk>/comment_update/", views.comment_update, name="comment_update"),
]
