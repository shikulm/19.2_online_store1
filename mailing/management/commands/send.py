from mailing.services import send_mails
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mails()

