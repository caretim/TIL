from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import A_Form, C_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    articles = Article.objects.all()
    comment_list = []
    for art in articles:
        comment_list.append(art.comment_set.all())  # 댓글의객체 이걸

    article_info = zip(articles, comment_list)
    context = {"articles": article_info}

    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = A_Form(request.POST)
        if form.is_valid():
            fform = form.save(commit=False)
            fform.user = request.user
            fform.save()
            return redirect("articles:index")
    else:
        form = A_Form()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


@login_required
def update(request, pk):
    a = Article.objects.get(pk=pk)
    if a.user == request.user:
        if request.method == "POST":
            form = A_Form(request.POST, instance=a)
            if form.is_valid():
                form.save()
                return redirect("articles:detail", pk)
        else:
            form = A_Form(instance=a)
        context = {"form": form}
        return render(request, "articles/create.html", context)
    else:
        return redirect("articles:detail", pk)


@login_required
def delete(request, pk):
    a = Article.objects.get(pk=pk)
    if a.user == request.user:
        Article.objects.get(pk=pk).delete()
        return redirect("articles:index")
    else:
        messages.warning(request, "작성자가 아닙니다.")
        return redirect("articles:index")


def detail(request, pk):
    detail_data = Article.objects.get(pk=pk)
    comment = detail_data.comment_set.all()
    if request.method == "POST":
        form = C_Form(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.article = detail_data
            a.user = request.user
            a.save()
        return redirect("articles:detail", detail_data.pk)
    else:
        form = C_Form()
    context = {
        "detail_data": detail_data,
        "form": form,
        "comment": comment,
    }
    return render(request, "articles/detail.html", context)


@login_required
def comment_update(request, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.user == request.user:
        if request.method == "POST":
            form = C_Form(request.POST, instance=comment)
            if form.is_valid():
                a = form.save(commit=False)
                a.article = comment.article
                a.user = request.user
                a.save()
                return redirect("articles:detail", pk)
        else:
            form = C_Form(instance=comment)
        context = {
            "form": form,
        }
        return render(request, "articles/detail.html", context)
    else:
        return redirect("articles:detail", pk)


@login_required
def delete_comment(request, pk):
    a = Comment.objects.get(pk=pk)
    if a.user == request.user:
        Comment.objects.get(pk=pk).delete()
        return redirect("articles:index")
    else:
        messages.warning(request, "작성자가 아닙니다.")
        return redirect("articles:detail", pk)
