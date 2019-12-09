from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from django.http import HttpResponse

import csv

class Command(BaseCommand):
    help = 'Export data'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help='filepath name')

    def handle(self, *args, **kwargs):
        meta = Squirrel._meta
        field_names = [i.name for i in meta.fields]
        file_path = kwargs['file_path']
        print(file_path)
        with open(file_path,'w') as csvfile:
            data_ = csv.writer(csvfile)
            data_.writerow(field_names)
            for obj in Squirrel.objects.all():
                data_.writerow([getattr(obj, field) for field in field_names])
