import sys

from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Sends a test email to verify mail configuration"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="The email address to send the test mail to")

    def handle(self, *args, **options):
        recipient_email = options["email"]

        subject = "Test Email from Django"
        message = "This is a test email sent from Django to verify the mail configuration."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [recipient_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            self.stdout.write(self.style.SUCCESS(f"Successfully sent test email to {recipient_email}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to send email: {e!s}"))
            sys.exit(1)
