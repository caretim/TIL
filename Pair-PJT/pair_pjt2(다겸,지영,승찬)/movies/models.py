from calendar import c
from django.db import models

RATE_CHOICES = (
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★"),
)

genre_table = (
    ("액션", "액션"),
    ("스릴러", "스릴러"),
    ("코미디", "코미디"),
    ("로맨스", "로맨스"),
    ("SF", "SF"),
    ("드라마", "드라마"),
    ("애니메이션", "애니메이션"),
)

title_table = (
    ("인생은 아름다워", "인생은 아름다워"),
    ("정직한 후보 2", "정직한 후보 2"),
    ("공조2: 인터내셔날", "공조2: 인터내셔날"),
    ("듄", "듄"),
    ("극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교", "극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교"),
    ("스마일", "스마일"),
    ("인터스텔라", "인터스텔라"),
    ("티켓 투 파라다이스", "티켓 투 파라다이스"),
)


class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30, choices=title_table)
    grade = models.IntegerField(choices=RATE_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    genre = models.CharField(max_length=5, choices=genre_table)

class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    movie_conent = models.TextField()