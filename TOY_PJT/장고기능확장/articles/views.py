from django.shortcuts import render, redirect
from .models import article
from .forms import MakeArticle

# Create your views here.


def article_index(request):
    all_data = article.objects.all()
    contetxt = {"all_data": all_data}
    return render(request, "articles/index.html", contetxt)


def create(request):
    if request.method == "POST":
        form = MakeArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("articles:index")
    else:
        form = MakeArticle()

    context = {"form": form}

    return render(request, "articles/create.html", context)


def update(request, pk):
    pick_data = article.objects.get(pk=pk)
    if request.method == "POST":
        form = MakeArticle(
            request.POST,
        )
        if form.is_valid():
            form.save()
        return redirect("articles:detail")
    else:
        form = MakeArticle(instance=pick_data)

    context = {"form": form}

    return render(request, "articles/update.html", context)


def detail(request, pk):
    pick_data = article.objects.get(pk=pk)
    context = {"pick_data": pick_data}

    return render(request, "articles/detail.html", context)


def delete(request, pk):
    article.objects.get(pk=pk).delete()
    return redirect("articles:index")
