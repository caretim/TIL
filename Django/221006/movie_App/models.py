from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.TextField(max_length=30)
    summary = models.TextField()
    running_time = models.TextField()
