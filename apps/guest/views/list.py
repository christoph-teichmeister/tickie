from django.views import generic

from apps.guest.models import Guest


class GuestListView(generic.ListView):
    model = Guest
    template_name = "guest/list.html"
