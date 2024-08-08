from ambient_toolbox.view_layer.views import RequestInFormKwargsMixin
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from apps.account.forms.login import LoginForm
from apps.account.models import User


class LoginView(RequestInFormKwargsMixin, generic.FormView):
    template_name = "account/login.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        self.success_url = reverse_lazy("event:list")

        request_user = self.request.user
        if request_user.role == User.RoleChoices.CHECK_IN_SECURITY:
            if request_user.works_for_events.count() == 1:
                self.success_url = reverse_lazy(
                    "guest:list", kwargs={"event_id": request_user.works_for_events.first().pk}
                )

        return super().get_success_url()
