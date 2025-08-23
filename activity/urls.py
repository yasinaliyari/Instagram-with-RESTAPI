from django.urls import path
from activity.views import CommentListCreateAPIView

urlpatterns = [
    path("comment/create/", CommentListCreateAPIView.as_view(), name="comment-create")
]
