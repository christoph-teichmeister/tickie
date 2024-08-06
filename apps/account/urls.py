from django.urls import path

from apps.account.views import login

app_name = "account"

urlpatterns = [
    path("login/", login.LoginView.as_view(), name="login"),
]
