from ambient_toolbox.admin.model_admins.mixins import CommonInfoAdminMixin
from django.contrib import admin

from apps.check_in.models import CheckIn


@admin.register(CheckIn)
class CheckInAdmin(CommonInfoAdminMixin, admin.ModelAdmin):
    list_display = ("__str__", "guest", "event")
    search_fields = ("guest__email", "event__name")
