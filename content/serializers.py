from rest_framework import serializers
from activity.serializers import CommentListSerializer
from content.models import Tag, Post, PostMedia
from location.serializers import LocationSerializer


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "title",
        )


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
            "id",
            "title",
            "posts",
        )

    def get_posts(self, obj):
        return obj.posts.count()


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = (
            "id",
            "media_type",
            "media_file",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    location = LocationSerializer()
    media = PostMediaSerializer(many=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "caption",
            "user",
            "location",
            "media",
            "comments",
        )

    def get_comments(self, obj):
        serializer = CommentListSerializer(
            obj.comments.filter(reply_to__isnull=True), many=True
        )
        return serializer.data
