from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.account.views import login, logout

app_name = "account"

urlpatterns = [
    path("login/", login.LoginView.as_view(), name="login"),
    path("logout/", login_required(logout.LogoutView.as_view()), name="logout"),
]
