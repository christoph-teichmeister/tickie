from ambient_toolbox.admin.model_admins.mixins import CommonInfoAdminMixin
from django.contrib import admin

from apps.guest.models.guest import Guest


@admin.register(Guest)
class GuestAdmin(CommonInfoAdminMixin, admin.ModelAdmin):
    list_display = ("email", "event", "status")
    list_filter = ("status",)
    search_fields = ("email", "event__name")
