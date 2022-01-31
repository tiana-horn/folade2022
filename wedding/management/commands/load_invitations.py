from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from wedding.models import Invitation, Guest, Event
from django.core.files import File


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'invitations', file)

class Command(BaseCommand):
    help = "Load invitations onto site"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
		
        print("Deleting invitations")
	    Invitation.objects.all().delete()
        with open(get_path('invitations.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                invitation = Invitation(
                    guest=Guest.objects.get(name=row['guest']),
                    event=Event.objects.get(name=row['event']),
                    attending=row['attending'],
                )
                invitation.save()
        print(f"{i} invitations loaded!")   
