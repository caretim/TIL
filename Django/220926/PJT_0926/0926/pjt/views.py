from email import contentmanager
from multiprocessing import context
from urllib import request
from django.shortcuts import render
import random

# Create your views here.
def index(request):

    return render(request, "index.html")


def ping(request):

    return render(request, "ping.html")


def pong(request):
    name = request.GET.get("going")
    context = {
        "name": name,
    }
    return render(request, "pong.html", context)


def fake_search(request):

    return render(request, "fake_search.html")


def odd_even(request, id):
    oddeven = "숫자를 입력해주세요"

    if id == 0:
        oddeven = "0"
    elif id % 2 == 1:
        oddeven = "홀수"
    elif id % 2 == 0:
        oddeven = "짝수"

    content = {"oddeven": oddeven}

    return render(request, "odd-even.html", content)


def calculate(request, id_a, id_b):

    idp = id_a + id_b
    idm = id_a - id_b
    idx = id_a * id_b
    idd = id_a // id_b

    content = {
        "idp": idp,
        "idm": idm,
        "idx": idx,
        "idd": idd,
        "id_a": id_a,
        "id_b": id_b,
    }

    return render(request, "calculate.html", content)


def before(request):

    return render(request, "before.html")


def before2(request):
    name = request.GET.get("pname")

    belife = 0

    lion = "사자"
    hama = "하마"
    humun = "인간"
    dog = "개"

    lifenum = random.choice("1234")

    if lifenum == "1":
        belife = lion
    elif lifenum == "2":
        belife = hama
    elif lifenum == "3":
        belife = humun
    else:
        belife = dog

    content = {
        "name": name,
        "belife": belife,
    }
    return render(request, "before2.html", content)


def hsum(request):

    return render(request, "hsum.html")


def makehsum(request):
    names = ["치킨", "라면", "짜짱면", "양갈비", "수박", "멜론", "치즈"]
    para = int(request.GET.get("para"))
    word = int(request.GET.get("word"))

    pword = [[] for __ in range(para)]

    for w in range(len(pword)):
        for _ in range(word):
            ran = random.choice(names)
            pword[w].append(ran)

    content = {"pword": pword}

    return render(request, "makehsum.html", content)
