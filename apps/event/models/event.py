from ambient_toolbox.models import CommonInfo
from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(CommonInfo):
    name = models.CharField(verbose_name=_("Name"), max_length=200)

    date_start = models.DateField(verbose_name=_("Start date"))
    date_end = models.DateField(verbose_name=_("End date"))

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("date_start",)

    def __str__(self):
        return self.name
