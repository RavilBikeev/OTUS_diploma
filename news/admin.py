from django.contrib import admin
from .models import News, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "created_at"]
    list_filter = ["is_published", "tags"]
    search_fields = ["title"]
    filter_horizontal = ["tags"]
