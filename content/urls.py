from django.urls import path

from content.views import TagListAPI, TagDetailAPI

urlpatterns = [
    path("tags/", TagListAPI.as_view(), name="tags-list"),
    path("tag/<int:pk>/", TagDetailAPI.as_view(), name="tags-detail"),
]
