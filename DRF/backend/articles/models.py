from django.db import models
from accounts.models import User
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles_user",
        null=True,
        blank=True,
    )
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pick(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pick_user",
        null=True,
        blank=True,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="pick_article",
        null=True,
        blank=True,
    )
    AB = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment_user",
        null=True,
        blank=True,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comment_article",
        null=True,
        blank=True,
    )
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
