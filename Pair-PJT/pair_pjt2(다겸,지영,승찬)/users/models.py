from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    join_at = models.DateTimeField(auto_now_add=True, verbose_name="가입시간")

    class Meta:
        db_table = "test_user"
