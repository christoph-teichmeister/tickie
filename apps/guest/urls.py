from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.guest.views import list

app_name = "guest"

urlpatterns = [
    path("list/<int:event_id>/", login_required(list.GuestListView.as_view()), name="list"),
]
