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

# user_post_detail = UserPostViewSet.as_view(
#     {"get": "retrieve", "put": "update", "delete": "destroy"}
# )
# user_post_list = UserPostViewSet.as_view({"get": "list", "post": "create"})
urlpatterns = [
    path("tags/", TagListAPI.as_view(), name="tags-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tags-create"),
    path("tag/<int:pk>/", TagDetailAPI.as_view(), name="tags-detail"),
    # path("post/<int:pk>/", PostDetailAPI.as_view(), name="post-detail"),
    # path(
    #     "user/posts/<int:user_id>/",
    #     UserPostsListAPIView.as_view(),
    #     name="user-posts-list",
    # ),
    # path("user/<str:username>/posts/", user_post_list, name="user_post_list"),
    # path(
    #     "user/<str:username>/posts/<int:pk>/", user_post_detail, name="user_post_detail"
    # ),
    path("user/<str:username>/", include(router.urls)),
]
