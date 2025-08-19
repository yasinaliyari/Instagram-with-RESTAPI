from django.urls import path

from content.views import TagListAPI

urlpatterns = [
    path("tags/", TagListAPI.as_view(), name="tags-list"),
]
