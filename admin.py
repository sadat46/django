from django.contrib import admin

# Register your models here.
from .models import MovieInfo, SongInfo

admin.site.register(MovieInfo)
admin.site.register(SongInfo)