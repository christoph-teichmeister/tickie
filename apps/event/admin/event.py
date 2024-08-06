from ambient_toolbox.admin.model_admins.mixins import CommonInfoAdminMixin
from django.contrib import admin

from apps.event.models import Event


@admin.register(Event)
class EventAdmin(CommonInfoAdminMixin, admin.ModelAdmin):
    list_display = ("name", "date_start", "date_end")
    list_filter = ("date_start",)
    search_fields = ("name",)
