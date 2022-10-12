from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review, Movie
from django.core.paginator import Paginator


def index(request):
    reviews = Review.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(reviews, 10)
    page_obj = paginator.get_page(page)
    context = {
        "reviews": reviews,
        "page_obj": page_obj,
    }
    return render(request, "movies/index.html", context)


def create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            post = review_form.save(commit=False)
            post.author = request.user
            # author 속성에 로그인 계정 저장
            return redirect("movies:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "movies/create.html", context)


def main(request):
    img_list = [
        {
            "num": 2,
            "img": "https://an2-img.amz.wtchn.net/image/v2/chphdsVeY3rZbgV09N1kSw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qSTFNekUyT0RBM016azRPVE00TlRRaWZRLjE0aGxoN2lkS3dZX1ZqVWd2MHlJeEpULXV3WlZRcjU1dllMNnVVaEVCc0U",
        },
        {
            "num": 3,
            "img": "https://an2-img.amz.wtchn.net/image/v2/8_d-c7PXw6gZ4kbRV0z4EA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qSTFNekU1TVRJeE1EWXlNRGN4T0RraWZRLnNLb1ZqWTIxcnZscXZnR2xVOVNRTnJQcEpoUHl6bTRLaG1YUTl5SFNwMnM",
        },
        {
            "num": 4,
            "img": "https://an2-img.amz.wtchn.net/image/v2/A3w93ZJKG1mmpfhnT4fviA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTJPVFF4TWprMU1EVTROakkwTVRjaWZRLjhlVmVkcUhkQzVSa1E3R1VCc1lKSG92aW9KdlZRSDljTk00UmVyYk1ibnM",
        },
        {
            "num": 5,
            "img": "https://an2-img.amz.wtchn.net/image/v2/LORpaHa1ccOKSEB_1aS6SA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk16STNPVEU0TWprek1ERXpOVGd5TkRraWZRLkcxY2d5eFQzY193WmhINm5wUkdZTFFKRmJDbHVoai1sME9wUDNMMFV0aUE",
        },
        {
            "num": 6,
            "img": "https://an2-img.amz.wtchn.net/image/v2/b-HjLSBuEhkWB1VylnIeyA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTXpNVE15TkRnME5UWTRNakEwT0RJaWZRLmp4Qk9lS3MtdnVrU093V1k0NFpfVjBoWUlUUE9WT3JiOFhKclM0UTJuVWc",
        },
        {
            "num": 7,
            "img": "https://an2-img.amz.wtchn.net/image/v2/Oa-1ShMGkP6KeN0oMtbysQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTTRNVE0zTURZME9EVXhNamN4TXpBaWZRLkk4dF80SkZLQkQ3Tld1c3JQMXR3Y1R1UkRPUW5CNVliemNzM0NlamdEWjQ",
        },
        {
            "num": 8,
            "img": "https://an2-img.amz.wtchn.net/image/v2/bw4jfVYFEl8JQKAtu6btTA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXhMM2x5WVRKM1pqRmtOSFJoYkc5NU5YRXpPWFYzSW4wLmF5Wk5HNmhtejZsVF9UVU83ZXpYV015ak95UDZVdkR5ZlRNTzJKX2NVUG8",
        },
        {
            "num": 9,
            "img": "https://an2-img.amz.wtchn.net/image/v2/jSs8bTuAHmCKAs7W_B730A.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTTRNVFF4TXpnMk1EY3pNVGt5T1RnaWZRLnNmOTMtay1qbG0zN1F6a0taSkg3RWdWUjc3SlNaSktHcE5sMEZSNlJxOTA",
        },
    ]

    context = {
        "img_list": img_list,
    }
    return render(request, "movies/main.html", context)


def detail(request, pk):
    review_get = Review.objects.get(pk=pk)

    context = {"review_get": review_get}

    return render(request, "movies/detail.html", context)


def update(request, pk):
    update_movie = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=update_movie)
        if review_form.is_valid():
            review_form.save()
            return redirect("movies:detail", pk)
    else:
        review_form = ReviewForm(instance=update_movie)
    context = {
        "review_form": review_form,
        "update_movie": update_movie,
    }
    return render(request, "movies/create.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("movies:index")


def search(request):
    all_movie = Review.objects.all()
    search_movie = request.GET.get("search", "")

    if search_movie:
        return_movie = all_movie.filter(title__icontains=search_movie)

    if len(search_movie) == 0:
        none_info = "공백을 입력하셨습니다."
        context = {
            "none_info": none_info,
        }
        return render(request, "movies/index.html", context)

    elif len(return_movie) > 0:
        context = {
            "search_movie": return_movie,
            "search_word": search_movie,
        }
        return render(request, "movies/index.html", context)

    elif len(return_movie) == 0:

        noinfo = "검색 결과가 없습니다"
        context = {
            "noinfo": noinfo,
        }
        return render(request, "movies/index.html", context)


def genres(request, pk):

    genres_table = {
        1: "액션",
        2: "스릴러",
        3: "코미디",
        4: "로맨스",
        5: "SF",
        6: "드라마",
        7: "애니메이션",
    }
    result_genre = genres_table.get(pk)
    all_genre = Review.objects.filter(genre=result_genre)

    context = {"all_genre": all_genre, "result_genre": result_genre}

    return render(request, "movies/index.html", context)


def movie(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Movie.objects.create(movie_title=title, movie_conent=content)
    return render(request, "movies/movie.html")


def make(request):
    return render(request, "movies/make.html")


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_get_title = movie.movie_title
    movie_filter = Review.objects.filter(movie_name=movie_get_title)

    dt_img_list = {
        2: "https://an2-img.amz.wtchn.net/image/v2/chphdsVeY3rZbgV09N1kSw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qSTFNekUyT0RBM016azRPVE00TlRRaWZRLjE0aGxoN2lkS3dZX1ZqVWd2MHlJeEpULXV3WlZRcjU1dllMNnVVaEVCc0U",
        3: "https://an2-img.amz.wtchn.net/image/v2/8_d-c7PXw6gZ4kbRV0z4EA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qSTFNekU1TVRJeE1EWXlNRGN4T0RraWZRLnNLb1ZqWTIxcnZscXZnR2xVOVNRTnJQcEpoUHl6bTRLaG1YUTl5SFNwMnM",
        4: "https://an2-img.amz.wtchn.net/image/v2/A3w93ZJKG1mmpfhnT4fviA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTJPVFF4TWprMU1EVTROakkwTVRjaWZRLjhlVmVkcUhkQzVSa1E3R1VCc1lKSG92aW9KdlZRSDljTk00UmVyYk1ibnM",
        5: "https://an2-img.amz.wtchn.net/image/v2/LORpaHa1ccOKSEB_1aS6SA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk16STNPVEU0TWprek1ERXpOVGd5TkRraWZRLkcxY2d5eFQzY193WmhINm5wUkdZTFFKRmJDbHVoai1sME9wUDNMMFV0aUE",
        6: "https://an2-img.amz.wtchn.net/image/v2/b-HjLSBuEhkWB1VylnIeyA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTXpNVE15TkRnME5UWTRNakEwT0RJaWZRLmp4Qk9lS3MtdnVrU093V1k0NFpfVjBoWUlUUE9WT3JiOFhKclM0UTJuVWc",
        7: "https://an2-img.amz.wtchn.net/image/v2/Oa-1ShMGkP6KeN0oMtbysQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTTRNVE0zTURZME9EVXhNamN4TXpBaWZRLkk4dF80SkZLQkQ3Tld1c3JQMXR3Y1R1UkRPUW5CNVliemNzM0NlamdEWjQ",
        8: "https://an2-img.amz.wtchn.net/image/v2/bw4jfVYFEl8JQKAtu6btTA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXhMM2x5WVRKM1pqRmtOSFJoYkc5NU5YRXpPWFYzSW4wLmF5Wk5HNmhtejZsVF9UVU83ZXpYV015ak95UDZVdkR5ZlRNTzJKX2NVUG8",
        9: "https://an2-img.amz.wtchn.net/image/v2/jSs8bTuAHmCKAs7W_B730A.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTTRNVFF4TXpnMk1EY3pNVGt5T1RnaWZRLnNmOTMtay1qbG0zN1F6a0taSkg3RWdWUjc3SlNaSktHcE5sMEZSNlJxOTA",
    }

    poster_img = dt_img_list.get(pk)

    context = {"movie": movie, "movie_filter": movie_filter, "poster_img": poster_img}
    return render(request, "movies/movie_detail.html", context)
