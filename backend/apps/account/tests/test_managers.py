from io import StringIO

import pytest
from django.core.management import call_command

from apps.account.models import User


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user(
            email="john@example.com",
            password="something-r@nd0m!",
        )
        assert user.email == "john@example.com"
        assert not user.is_staff
        assert not user.is_superuser
        assert user.check_password("something-r@nd0m!")
        assert user.username is None

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="admin@example.com",
            password="something-r@nd0m!",
        )
        assert user.email == "admin@example.com"
        assert user.is_staff
        assert user.is_superuser
        assert user.username is None

    def test_create_superuser_username_ignored(self):
        user = User.objects.create_superuser(
            email="test@example.com",
            password="something-r@nd0m!",
        )
        assert user.username is None

    def test_create_superuser_must_staff(self):
        with pytest.raises(ValueError, match="Superuser must have is_staff=True."):
            User.objects.create_superuser(email="test@example.com", password="something-r@nd0m!", is_staff=False)

    def test_create_superuser_must_superuser(self):
        with pytest.raises(ValueError, match="Superuser must have is_superuser=True."):
            User.objects.create_superuser(email="test@example.com", password="something-r@nd0m!", is_superuser=False)

    def test_create_user_without_email_raises(self):
        """Test that a user cannot be created without email"""
        with pytest.raises(ValueError, match="The given email must be set"):
            User.objects.create_user(
                password="something-r@nd0m!",
                email=None,
            )


@pytest.mark.django_db
def test_createsuperuser_command():
    """Ensure createsuperuser command works with our custom manager."""
    out = StringIO()
    command_result = call_command(
        "createsuperuser",
        "--email",
        "henry@example.com",
        interactive=False,
        stdout=out,
    )

    assert command_result is None
    assert out.getvalue() == "Superuser created successfully.\n"
    user = User.objects.get(email="henry@example.com")
    assert not user.has_usable_password()
