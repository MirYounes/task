from django.contrib import admin
from .models import Rating


@admin.register(Rating)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'rate']
