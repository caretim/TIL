from django.shortcuts import render, redirect
from .models import article
from .forms import MakeArticle
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.


def article_index(request):
    all_data = article.objects.all()
    contetxt = {"all_data": all_data}
    return render(request, "articles/index.html", contetxt)


@login_required
def create(request):
    if request.method == "POST":
        aform = MakeArticle(request.POST, request.FILES)
        if aform.is_valid():
            post = aform.save(commit=False)
            post.user = request.user
            post.save()

        return redirect("articles:index")
    else:
        form = MakeArticle()
    context = {
        "form": form,
    }

    return render(request, "articles/create.html", context)


@login_required
def update(request, pk):
    pick_data = article.objects.get(pk=pk)
    if pick_data.user == request.user:
        if request.method == "POST":
            form = MakeArticle(request.POST, request.FILES, instance=pick_data)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
            return redirect("articles:detail", pick_data.pk)
        else:
            form = MakeArticle(instance=pick_data)
        context = {"form": form}
        return render(request, "articles/update.html", context)


def detail(request, pk):
    pick_data = article.objects.get(pk=pk)
    context = {"pick_data": pick_data}

    return render(request, "articles/detail.html", context)


@login_required
def delete(request, pk):
    article.objects.get(pk=pk).delete()
    return redirect("articles:index")
