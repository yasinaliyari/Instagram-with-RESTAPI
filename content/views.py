from rest_framework.authentication import SessionAuthentication
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


class UserPostReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    lookup_url_kwarg = "pk"
    serializer_class = PostDetailSerializer
    pagination_class = StandardCursorPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__username=self.kwargs["username"])
