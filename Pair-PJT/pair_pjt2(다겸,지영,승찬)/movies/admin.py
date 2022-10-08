from django.contrib import admin
from .models import Review
from .models import Movie

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content')

admin.site.register(Movie)