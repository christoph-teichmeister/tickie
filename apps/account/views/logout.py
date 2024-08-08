from django.contrib.auth import logout
from django.views import generic


class LogoutView(generic.RedirectView):
    pattern_name = "account:login"

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)
