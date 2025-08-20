from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag


class TagDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, **{"pk": pk})

        return Response(
            {
                "id": tag.id,
                "title": tag.title,
                "posts": tag.posts.count(),
            },
            status=status.HTTP_200_OK,
        )


class TagListAPI(APIView):
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()

        data = list()

        for tag in tags:
            data.append(
                {
                    "id": tag.id,
                    "title": tag.title,
                    "posts": tag.posts.count(),
                }
            )
        return Response(data, status=status.HTTP_200_OK)
