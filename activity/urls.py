from django.urls import path
from activity.views import (
    CommentListCreateAPIView,
    CommentRetrieveAPIView,
    LikeCreateAPIView,
)

urlpatterns = [
    path("comment/create/", CommentListCreateAPIView.as_view(), name="comment-create"),
    path("like/<int:pk>/create/", LikeCreateAPIView.as_view(), name="like-create"),
    path(
        "comment/retrieve/<int:some_key>/",
        CommentRetrieveAPIView.as_view(),
        name="comment-retrieve",
    ),
]
