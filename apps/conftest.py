import factory
import pytest
from django.conf import settings
from django.utils import translation
from django_pony_express.services.tests import EmailTestService

import apps.account.tests.factories as account_factories
from apps.account.models import User


@pytest.hookimpl(hookwrapper=True)
def pytest_runtestloop(session):
    """
    Sets default locale of Faker to `settings.LANGUAGE_CODE`.

    Refer to: https://faker.readthedocs.io/en/master/locales/de_DE.html
    """

    with factory.Faker.override_default_locale(translation.to_locale(settings.LANGUAGE_CODE)):
        yield


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    """
    Returns a User with a valid Token.
    """

    return account_factories.UserFactory()


@pytest.fixture
def email_test_service():
    """
    Returns the mail tester from pony express.
    """

    return EmailTestService()
