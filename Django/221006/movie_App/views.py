from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Movie
from .forms import movie_Form


# Create your views here.


def index(request):
    all_movie = Movie.objects.all().order_by("id")

    context = {
        "all_movie": all_movie,
    }

    return render(request, "movies/index.html", context)


def detail(request, pk):
    detail = Movie.objects.get(pk=pk)
    context = {
        "detail": detail,
    }
    return render(request, "movies/index.html", context)


def create(requset):
    if requset.method == "POST":
        form = movie_Form(requset.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_App:index")
    else:
        form = movie_Form()
        context = {"form": form}

        return render(requset, "movies/create.html", context)


def delete(requset, pk):

    movie_delete = Movie.objects.get(pk=pk).delete()

    return redirect("movie_App:index")


def update(request, pk):
    update_movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        form = movie_Form(request.POST, instance=update_movie)
        if form.is_valid():
            form.save()
        return redirect("movie_App:detail", update_movie.pk)
    else:
        form = movie_Form(instance=update_movie)
        context = {
            "form": form,
            "update_movie": update_movie,
        }

        return render(request, "movies/update.html", context)
