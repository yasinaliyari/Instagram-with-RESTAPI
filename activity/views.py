from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from activity.models import Comment
from activity.serializers import CommentCreateSerializer, CommentListSerializer


class CommentListCreateAPIView(CreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return self.serializer_class


class CommentRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "some_key"
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class
        return CommentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
