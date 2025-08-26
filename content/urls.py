from django.urls import path

from content.views import (
    TagListAPI,
    TagDetailAPI,
    PostDetailAPI,
    TagCreateAPIView,
    UserPostsListAPIView,
    UserPostReadOnlyViewSet,
)

user_post_detail = UserPostReadOnlyViewSet.as_view({"get": "retrieve"})
user_post_list = UserPostReadOnlyViewSet.as_view({"get": "list"})
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
    path("user/<str:username>/posts/", user_post_list, name="user_post_list"),
    path(
        "user/<str:username>/posts/<int:pk>/", user_post_detail, name="user_post_detail"
    ),
]
