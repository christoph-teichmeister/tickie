from django.db import models

from apps.event.querysets.event import EventQuerySet


class EventManager(models.Manager.from_queryset(EventQuerySet)):
    pass
