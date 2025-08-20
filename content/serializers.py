from rest_framework import serializers
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
        )

    def get_posts(self, obj):
        return obj.posts.count()
