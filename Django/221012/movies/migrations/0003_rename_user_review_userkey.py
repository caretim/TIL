# Generated by Django 3.2.13 on 2022-10-12 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221013_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='userkey',
        ),
    ]
