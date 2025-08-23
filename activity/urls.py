from django.urls import path
from activity.views import CommentCreateAPIView

urlpatterns = [
    path("comment/create/", CommentCreateAPIView.as_view(), name="comment-create")
]
