from ambient_toolbox.models import CommonInfo
from django.db import models
from django.utils.translation import gettext_lazy as _


class Guest(CommonInfo):
    class StatusChoices(models.IntegerChoices):
        CREATED = 0, _("Created")
        INVITED = 1, _("Invited")
        ACCEPTED = 2, _("Accepted")
        DECLINED = 3, _("Declined")

    email = models.EmailField(_("E-Mail"))
    status = models.SmallIntegerField(_("Status"), choices=StatusChoices.choices, default=StatusChoices.CREATED)

    event = models.ForeignKey(
        "event.Event",
        verbose_name=_("Event"),
        on_delete=models.CASCADE,
        help_text=_("The event this guest belongs to"),
        related_name="guest_list",
    )

    class Meta:
        verbose_name = _("Guest")
        verbose_name_plural = _("Guests")
        ordering = ("email",)

    def __str__(self):
        return self.email
