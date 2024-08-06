import pytest

from .factories import UserFactory


@pytest.mark.django_db
def test_userfactory_without_password():
    auth_user = UserFactory()

    assert auth_user.check_password("password") is False


@pytest.mark.django_db
def test_userfactory_with_password():
    auth_user = UserFactory(password="password")

    assert auth_user.check_password("password") is True
