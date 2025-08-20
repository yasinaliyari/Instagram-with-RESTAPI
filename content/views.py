from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag, Post
from content.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    PostDetailSerializer,
)


class TagDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, **{"pk": pk})
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListAPI(APIView):
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TagListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Post, **{"pk": pk})
        serializer = PostDetailSerializer(instance)
        return Response(serializer.data)
