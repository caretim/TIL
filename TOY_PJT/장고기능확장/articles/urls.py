from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "articles"

urlpatterns = [
    path("", views.article_index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like_user/", views.like_user, name="like_user"),
    path("<int:pk>/comment_delete/", views.comment_delete, name="comment_delete"),
]
