from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>", views.detail, name="detail"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    path("<int:pk>/genre", views.genres, name="genres"),
    path("movie/", views.movie, name="movie"),
    path("make/", views.make, name="make"),
    path("<int:pk>/movie_detail", views.movie_detail, name="movie_detail"),
]
