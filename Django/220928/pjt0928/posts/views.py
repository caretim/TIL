from django.shortcuts import render, redirect
from .models import post


# Create your views here.
def index(request):
    # 모든 글 보여주기
    # 1.db에서 모든 글을 불러온다.
    posts = post.objects.all()
    # 2.템플릿에 보내준다
    context = {"posts": posts}
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    post.objects.create(title=title, content=content)
    context = {
        "title": title,
        "content": content,
    }
    return redirect("posts:index")


def delete(request, pk):
    post.objects.get(id=pk).delete()

    return redirect("posts:index")
