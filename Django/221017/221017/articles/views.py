from django.shortcuts import render, redirect
from .form import MakeArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.


def index(request):
    all_date = Article.objects.all()
    context = {"all_date": all_date}

    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        form = MakeArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 작성 완료!")

        return redirect("articles:index")
    else:
        form = MakeArticleForm()
    context = {"form": form}

    return render(request, "articles/create.html", context)


def edit(request, pk):
    pick_data = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = MakeArticleForm(request.POST, request.FILES, instance=pick_data)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 수정 완료!")
        return redirect("articles:detail", pick_data.pk)
    else:
        form = MakeArticleForm(instance=pick_data)
    context = {
        "form": form,
        "pick_data": pick_data,
    }

    return render(request, "articles/edit.html", context)


def detail(request, pk):
    detail_data = Article.objects.get(pk=pk)

    context = {"detail_data": detail_data}

    return render(request, "articles/detail.html", context)


def delete(reuqest, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
