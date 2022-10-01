from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all().order_by("deadline")

    context = {"todos": _todos}

    return render(request, "todos/index.html", context)


def create(request):
    # k = request.GET
    # v = [k[i] for i in k]
    # silver.objects.create(content=v[0], priority=v[1], deadline=v[2])

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    # created_at = request.GET.get("created_at")
    deadline = request.GET.get("deadline")

    Todo.objects.create(
        content=content,
        priority=priority,
        # created_at=created_at,
        deadline=deadline,
    )

    return redirect("todos:index")


def delete(reuqest, todo_pk):

    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")


def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    context = {
        "todos": todo,
    }

    return render(request, "todos/edit.html", context)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        "todos": todo,
    }

    return render(request, "todos/datail.html", context)


# def update(request, todo_pk):
#     todo = Todo.objects.get(pk=todo_pk)

#     return redirect("todos:index")
