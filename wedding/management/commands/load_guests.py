from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from wedding.models import Guest
from django.core.files import File


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'guests', file)

class Command(BaseCommand):
    help = "Load invitations onto site"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):


        with open(get_path('guests.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                guest = Guest(
                    name=row['name'],
                    email=row['email'],
                    aso_ebi=row['aso_ebi'],
                    aso_ebi_paid=row['aso_ebi_paid'],
                    hotel_accomodations=row['hotel_accomodations'],
                    diet=row['diet'],
                    food_allergies=row['food_allergies'],
                )
                guest.save()
        print(f"{i} guestes loaded!")  
