from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _

from apps.account.managers.user import UserManager


class User(AbstractUser):
    """
    Default custom user model for tickie.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of user"), blank=True, max_length=255)
    first_name = None
    last_name = None

    email = EmailField(_("Email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
