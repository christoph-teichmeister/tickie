from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.event.views import list

app_name = "event"

urlpatterns = [
    path("list/", login_required(list.EventListView.as_view()), name="list"),
]
