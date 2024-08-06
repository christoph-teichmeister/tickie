import re
from http import HTTPStatus

import pytest
from _pytest.mark import param
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import all_sites
from django.db.models import Model
from django.urls import reverse

from apps.account.tests.factories import UserFactory


def make_url(site: AdminSite, model: type[Model], page: str) -> str:
    return reverse(f"{site.name}:{model._meta.app_label}_{model._meta.model_name}_{page}")


@pytest.mark.django_db
@pytest.mark.parametrize(
    "site,model,model_admin",
    [
        param(
            site,
            model,
            model_admin,
            id=f"{site.name}"
            + f"{re.sub(r'(?<!^)(?=[A-Z])', '_', str(model_admin)).lower().replace('.', '_').replace('__', '_')}",
        )
        for site in all_sites
        for model, model_admin in site._registry.items()
    ],
)
def test_admin(client, settings, site, model, model_admin):
    """
    Generic tests for admin "list" and "add" views.
    Source: https://adamj.eu/tech/2023/03/17/django-parameterized-tests-model-admin-classes/
    """

    settings.SECURE_SSL_REDIRECT = False

    client.force_login(UserFactory(is_superuser=True, is_staff=True))

    url = make_url(site, model, "changelist")
    response = client.get(url, {"q": "example.com"})
    assert response.status_code == HTTPStatus.OK

    url = make_url(site, model, "add")
    response = client.get(url)
    assert response.status_code in (
        HTTPStatus.OK,
        HTTPStatus.FORBIDDEN,  # some admin classes blanket disallow "add"
    )
