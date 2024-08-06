from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.account.managers.user import UserManager


class User(AbstractUser):
    """Default custom user model for tickie."""

    class RoleChoices(models.IntegerChoices):
        TICKIE_ADMIN = 0, _("Tickie Administrator")
        CHECK_IN_SECURITY = 1, _("Check In Security")

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of user"), blank=True, max_length=255)
    first_name = None
    last_name = None

    email = models.EmailField(_("Email address"), unique=True)
    username = None

    role = models.SmallIntegerField(_("Role"), choices=RoleChoices.choices, null=True, blank=True)
    works_for_events = models.ManyToManyField("event.Event", verbose_name=_("Works for events"), blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
