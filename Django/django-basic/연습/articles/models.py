from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)