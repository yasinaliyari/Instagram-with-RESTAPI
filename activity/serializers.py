from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from activity.models import Comment
from content.serializers import PostDetailSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("caption", "post", "reply_to")

    def validate(self, attrs):
        if len(attrs["caption"]) > 30:
            raise ValidationError("Caption cannot be more than 30 characters")
        return attrs


class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ("id", "caption", "reply_to", "user", "post")
