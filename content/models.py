from django.contrib.auth import get_user_model
from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _
from location.models import Location
from django.core.validators import FileExtensionValidator

User = get_user_model()


class Post(BaseModel):
    caption = models.TextField(_("caption"), blank=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, related_name="posts", on_delete=models.CASCADE, blank=True
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "{} ({})".format(self.user, self.id)
