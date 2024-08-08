from django.views import generic
from django_context_decorator import context

from apps.event.models import Event
from apps.guest.models import Guest


class GuestListView(generic.ListView):
    model = Guest
    template_name = "guest/list.html"

    def get_queryset(self):
        return super().get_queryset().filter(event_id=self.kwargs.get("event_id"))

    @context
    @property
    def event_name(self):
        return Event.objects.filter(id=self.kwargs.get("event_id")).first()
