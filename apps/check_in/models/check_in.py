from ambient_toolbox.models import CommonInfo
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class CheckIn(CommonInfo):
    checked_in_at = models.DateTimeField(_("Checked in at"))
    checked_out_at = models.DateTimeField(_("Checked out at"), null=True, blank=True)

    event = models.ForeignKey("event.Event", verbose_name=_("Event"), on_delete=models.CASCADE)
    guest = models.ForeignKey("guest.Guest", verbose_name=_("Guest"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Check In")
        verbose_name_plural = _("Check Ins")
        ordering = ("created_at",)

    def __str__(self):
        return _("%s: %s for %s") % (self.id, self.guest.email, self.event.name)

    def clean(self):
        super().clean()

        if self.checked_in_at.date() < self.event.date_start:
            raise ValidationError(
                {"checked_in_at": [_("The date of 'Checked in at' must be after the start date of the event")]}
            )

        if self.checked_out_at < self.checked_in_at:
            raise ValidationError({"checked_out_at": [_("Check out must happen after Check in")]})
