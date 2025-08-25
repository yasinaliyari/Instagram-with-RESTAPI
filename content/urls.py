from django.urls import path

from content.views import (
    TagListAPI,
    TagDetailAPI,
    PostDetailAPI,
    TagCreateAPIView,
    UserPostsListAPIView,
)

urlpatterns = [
    path("tags/", TagListAPI.as_view(), name="tags-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tags-create"),
    path("tag/<int:pk>/", TagDetailAPI.as_view(), name="tags-detail"),
    path("post/<int:pk>/", PostDetailAPI.as_view(), name="post-detail"),
    path(
        "user/posts/<int:user_id>/",
        UserPostsListAPIView.as_view(),
        name="user-posts-list",
    ),
]
