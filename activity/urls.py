from django.urls import path
from activity.views import (
    CommentListCreateAPIView,
    CommentRetrieveAPIView,
    CommentDestroyAPIView,
)

urlpatterns = [
    path("comment/create/", CommentListCreateAPIView.as_view(), name="comment-create"),
    path(
        "comment/retrieve/<int:some_key>/",
        CommentRetrieveAPIView.as_view(),
        name="comment-retrieve",
    ),
    path(
        "comment/destroy/<int:pk>/",
        CommentDestroyAPIView.as_view(),
        name="comment-destroy",
    ),
]
