from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
