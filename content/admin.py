from django.contrib import admin
from django.contrib.admin import register
from content.models import Post, Tag


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_time",
    )


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_time",
    )
