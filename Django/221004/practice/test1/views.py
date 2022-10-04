from django.shortcuts import render, redirect


from .models import tests

from .forms import test1Form


# Create your views here.

# 요청 정보를 받아서 페이지를 render한다.
def index(request):
    alldate = tests.objects.all()

    context = {
        "alldate": alldate,
    }

    return render(request, "test1/index.html", context)


# def new(request):
#


def create(request):
    # title_ = request.post.get("title")
    # content_ = request.post.get("content")
    test_form = test1Form(request.POST)
    if test_form.is_valid():
        test_form.save()
        return redirect("test1:index")

    else:
        context = {"test_form": test_form}
    return render(request, "test1/create.html", context)

    # tests.objects.create(
    #     title=title_,
    #     content=content_,
    # )


#
