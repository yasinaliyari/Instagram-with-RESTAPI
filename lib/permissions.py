from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission
from relation.models import Relation

User = get_user_model()


class RelationExists(BasePermission):
    message = _("You have not followed this account")

    def has_permission(self, request, view):
        user = User.objects.filter(id=view.kwargs["user_id"]).first()
        if user:
            return (
                Relation.objects.filter(from_user=request.user, to_user=user).exists()
                or request.user == user
            )
        return False


class HasPostPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            Relation.objects.filter(from_user=request.user, to_user=obj.user).exists()
            or request.user == obj.user
        )
