from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountConfig(AppConfig):
    name = "apps.account"
    verbose_name = _("Account")

    def ready(self):
        try:
            import apps.account.signals  # noqa: F401
        except ImportError:
            pass
