from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.account.forms.admin.change import UserAdminChangeForm
from apps.account.forms.admin.create import UserAdminCreateForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreateForm
    fieldsets = (
        (
            None,
            {"fields": ("email", "password")},
        ),
        (
            _("Personal info"),
            {"fields": ("name", "works_for_events")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )
    list_display = ("email", "name", "role", "is_superuser", "is_superuser")
    search_fields = ("name",)
    ordering = ("id",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
