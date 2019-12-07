Learn more or give us feedback
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Export the data in CSV format.'

    def handle(self, *args, **kwargs):
        with open('export_squirrel_data.csv', mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            all_fields = [a.name for a in Squirrel._meta.get_fields()]
            fieldnames = [Squirrel._meta.get_field(b).help_text for b in all_fields[1:]]
            writer.writerow(fieldnames)
            for i in range(len(Squirrel.objects.all())):
                rowval=list()
                for j in all_fields:
                    if j == 'id': continue
                    rowval.append(getattr(Squirrel.objects.all()[i],j))
                writer.writerow(rowval)
        csvfile.close
