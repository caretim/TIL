from dataclasses import field
from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Todo(models.Model):
    # django 에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length=80)
    """
    default: 데이터를 생성 할 때 값을 안넣으면
    자동으로 값을 채워서 데이터를 생성하겠다.
    """

    completed = models.BooleanField(default=False)

    priority = models.IntegerField(default=3)

    created_at = models.DateField(auto_now_add=TRUE)

    deadline = models.DateField(null=True)
