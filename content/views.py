from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.generics import (
    get_object_or_404,
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from activity.serializers import LikeSerializer
from content.models import Tag, Post
from content.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    PostDetailSerializer,
)
from lib.pagination import SmallPageNumberPagination, StandardCursorPagination
from lib.permissions import RelationExists
from rest_framework import viewsets


class TagDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, **{"pk": pk})
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListAPI(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallPageNumberPagination


class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class PostDetailAPI(RetrieveAPIView):
    permission_classes = [IsAuthenticated, RelationExists]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class UserPostsListAPIView(ListAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = "user_id"
    serializer_class = PostDetailSerializer
    pagination_class = StandardCursorPagination
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.kwargs[self.lookup_url_kwarg])


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    lookup_url_kwarg = "pk"
    serializer_class = PostDetailSerializer
    pagination_class = StandardCursorPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__username=self.kwargs["username"])

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, RelationExists]

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "get_likes_list":
            return LikeSerializer
        return self.serializer_class

    @action(detail=True)
    def get_likes_list(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.likes.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
