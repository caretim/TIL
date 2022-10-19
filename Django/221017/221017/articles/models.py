from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    img = ProcessedImageField(
        upload_to="image/",
        blank=True,
        processors=[ResizeToFill(1000, 300)],
        format="JPEG",
        options={"quality": 100},
    )
