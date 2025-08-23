from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from activity.models import Comment
from activity.serializers import CommentCreateSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
