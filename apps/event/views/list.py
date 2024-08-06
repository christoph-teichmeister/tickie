from django.views import generic

from apps.event.models import Event


class EventListView(generic.ListView):
    model = Event
    template_name = "event/list.html"

    def get_queryset(self):
        return super().get_queryset().visible_for(user=self.request.user)
