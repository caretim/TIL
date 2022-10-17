from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
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


class article(models.Model):
    userkey = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userkey"
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(choices=RATE_CHOICES)
    img = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(450, 300)],
        format="JPEG",
        options={"quality": 100},
    )


class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    summary = models.TextField()
    genre = models.CharField(max_length=80, choices=genre_table)
    start_at = models.DateField()
