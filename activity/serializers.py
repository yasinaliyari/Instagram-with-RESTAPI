from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from activity.models import Comment
from content.serializers import PostDetailSerializer
from django.utils.translation import gettext_lazy as _


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("caption", "post", "reply_to")

    def validate_caption(self, attr):
        if len(attr) > 30:
            raise ValidationError(_("Caption cannot be more than 30 characters"))
        return attr

    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValidationError(_("You cannot reply to a reply recursively"))
        return attr

    def validate(self, attrs):
        return attrs


class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ("id", "caption", "reply_to", "user", "post")
