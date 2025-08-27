from django.urls import path, include
from content.views import (
    TagListAPI,
    TagDetailAPI,
    PostDetailAPI,
    TagCreateAPIView,
    UserPostsListAPIView,
    UserPostViewSet,
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("post", UserPostViewSet, "user-post")

urlpatterns = [
    path("tags/", TagListAPI.as_view(), name="tags-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tags-create"),
    path("tag/<int:pk>/", TagDetailAPI.as_view(), name="tags-detail"),
    path("user/<str:username>/", include(router.urls)),
]
