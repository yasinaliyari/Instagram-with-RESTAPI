from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from activity.models import Comment
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


class CommentRepliesListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ("id", "caption", "user", "reply_to")


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "caption", "replies", "user")

    def get_replies(self, obj):
        qs = obj.replies.all()

        if qs.count() > 10:
            qs = qs[:10]

        serializer = CommentRepliesListSerializer(qs, many=True)
        return serializer.data
