from django.db import models
from django.conf import settings


# Create your models here.
RATE_CHOICES = (
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★"),
)
# user_id -> 이게 유니크 속성을 가지고있어서, 여러 키를 가질 수 없었는데,
# 요거를 유저아이디라는 컬럼으로 가져오는게 아니고, 이름을 다른걸로 지정하면,
# 유니크로 오지 않는다.!


class Review(models.Model):
    userkey = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userkey"
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(choices=RATE_CHOICES)


genre_table = (
    ("액션", "액션"),
    ("스릴러", "스릴러"),
    ("코미디", "코미디"),
    ("로맨스", "로맨스"),
    ("SF", "SF"),
    ("드라마", "드라마"),
    ("애니메이션", "애니메이션"),
)


class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    summary = models.TextField()
    genre = models.CharField(max_length=80, choices=genre_table)
    start_at = models.DateField()
