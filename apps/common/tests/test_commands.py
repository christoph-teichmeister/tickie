import pytest
from django.core import mail
from django.core.management import call_command


@pytest.mark.django_db
class TestVerifyMailCommand:
    def test_command_success(self, capsys):
        test_email = "test@example.com"

        call_command("verify_mail", test_email)

        captured = capsys.readouterr()
        assert f"Successfully sent test email to {test_email}" in captured.out
        assert len(mail.outbox) == 1
        assert mail.outbox[0].to == [test_email]

    def test_command_failure(self, mocker):
        test_email = "test@example.com"

        # Mock send_mail to raise an exception
        mocker.patch(
            "apps.common.management.commands.verify_mail.send_mail",
            side_effect=Exception("SMTP error"),
        )
        with pytest.raises(SystemExit) as excinfo:
            call_command("verify_mail", test_email)

        assert excinfo.value.code == 1

    def test_command_output(self, capsys):
        test_email = "test@example.com"

        call_command("verify_mail", test_email)

        captured = capsys.readouterr()
        assert "Test Email from Django" not in captured.out  # Subject should not be in output
        assert "This is a test email" not in captured.out  # Message should not be in output
