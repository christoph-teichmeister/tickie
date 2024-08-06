from django import forms
from django.contrib.auth import authenticate, user_login_failed
from django.utils.translation import gettext_lazy as _

from apps.account.models import User


class LoginForm(forms.Form):
    request = None

    email = forms.CharField(label=_("Email"), max_length=120, required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, required=True)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request

        super().__init__(*args, **kwargs)

    def get_user(self):
        return self.user_cache

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user_login_failed.send(sender=User, request=self.request, credentials={"email": email})
            raise forms.ValidationError(_("Invalid user and password combination.")) from None

        self.user_cache = authenticate(request=self.request, email=user.email, password=password)

        if self.user_cache is None:
            raise forms.ValidationError(_("Invalid user and password combination."))

        return self.cleaned_data
