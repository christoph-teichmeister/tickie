from django.db import models

from apps.account.models import User


class EventQuerySet(models.QuerySet):
    def visible_for(self, user: User):
        if user.is_superuser:
            return self

        if user.role == User.RoleChoices.CHECK_IN_SECURITY:
            return self.filter(id__in=user.works_for_events.all())

        return self.none()
