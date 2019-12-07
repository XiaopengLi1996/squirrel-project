from sightings.models import
import csv
from django.core.management import BaseCommand

class Command(BaseCommand):

    help = 'Import Data from the 2018 census file (in CSV format)'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        import datetime
        path = kwargs['path']
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if row[i] == 'false' or row[i] == 'FALSE':
                        row[i] = False
                    else:
                        row[i] = True
                longitude = row[0]
                latitude = row[1]
                unique_squirrel_id = row[2]
                shift = row[4]
                date = datetime.datetime.strptime(row[5],"%m%d%Y").strftime("%Y-%m-%d")
                age = row[7]
                primary_fur_color = row[8]
                location = row[12]
                specific_location = row[14]
                running = row[15]
                chasing = row[16]
                climbing = row[17]
                eating = row[18]
                foraging = row[19]
                other_activities = row[20]
                kuks = row[21]
                quaas = row[22]
                moans = row[23]
                tail_flags = row[24]
                tail_twitches = row[25]
                approaches = row[26]
                indifferent = row[27]
                run_from = row[28]

                db = squirrel(
			X = longitude, 
			Y = latitude, 
			Unique_Squirrel_ID = unique_squirrel_id, 
			Shift = shift, 
			Date = date, 
			Age = age, 
			Primary_Fur_Color = primary_fur_color, 
			Location = location, 
			Specific_Location = specific_location, 
			Running = running, 
			Chasing = chasing, 
			Climbing = climbing, 
			Eating = eating, 
			Foraging = foraging, 
			Other_Activities = other_activities, 
			Kuks = kuks, 
			Quaas=quaas, 
			Moans=moans, 
			Tail_flags = tail_flags, 
			Tail_twitches = tail_twitches, 
			Approaches = approaches, 
			Indifferent = indifferent, 
			Runs_from = run_from
			)
                db.save() 
