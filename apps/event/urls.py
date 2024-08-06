from django.urls import path

from apps.event.views import list

app_name = "event"

urlpatterns = [
    path("list/", list.EventListView.as_view(), name="list"),
]
