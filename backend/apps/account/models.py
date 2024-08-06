from typing import ClassVar

from ambient_toolbox.utils.string import slugify_file_name
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField
from django.utils.translation import gettext_lazy as _

from apps.account.managers import UserManager


def profile_image_upload_location(instance, filename):
    return f"user_{instance.id}/{slugify_file_name(filename)}"


class User(AbstractUser):
    """
    Default custom user model for tickie.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of user"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    profile_image = ImageField(_("Profile image"), upload_to=profile_image_upload_location, null=True)
    email = EmailField(_("Email address"), unique=True)
    username = None  # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()
