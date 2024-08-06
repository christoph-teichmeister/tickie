from django.urls import path

from apps.guest.views import list

app_name = "guest"

urlpatterns = [
    path("list/", list.GuestListView.as_view(), name="list"),
]
