from django.db import models

class Squirrel(models.Model):
    
    X = models.DecimalField(
	max_digits = 20,
	decimal_places = 17,
	help_text = "Location's Longitude",
        null = True,
	blank = True,
	)

    Y = models.DecimalField(
	max_digits = 20, 
        decimal_places = 17,
        help_text = "Location's Latitude",
        null = True, 
	blank = True,
        ) 

    Unique_Squirrel_ID = models.CharField(
	max_length = 14,
	help_text = "Unique Squirrel ID",
        primary_key = True,
	) 

    AM = 'AM'
    PM = 'PM'
    
    Shift_Choices = [
	(AM, 'AM'),
	(PM, 'PM'),
    ] 

    Shift = models.CharField(
	choices = Shift_Choices,
	default = AM,
	max_length = 2,
	null = True,
	help_text = "Shift",
        blank = True,
	)

    Date = models.DateField(
	help_text = "Date",
	null = True,
	blank = True,
	)
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    
    Age_Choices = [
	(Adult , 'Adult'),
	(Juvenile , 'Juvenile'),
	(Unknown , '?'),
    ]

    Age = models.CharField(
	choices = Age_Choices,
	max_length = 8,
	blank = True,
	help_text = "Age",
	)
    
    Gray = 'Gray'
    Black = 'Black'
    Cinnammon = 'Cinnammon'

    Color_Choices = [
	(Gray, 'Gray'),
	(Black, 'Black'),
	(Cinnammon, 'Cinnammon'),
    ]

    Primary_Fur_Color = models.CharField(
	choices = Color_Choices,
	max_length = 10,
	blank = True,
	null = True,
	help_text = "Primary Fur Color",
	)

    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground Plane'    

    Loc_Choices = [ 
	(Above_Ground, 'Above Ground'),
	(Ground_Plane, 'Ground Plane'),
    ]
	
    Location = models.CharField(
	choices = Loc_Choices,
	max_length = 15,
	blank = True,
	null = True,
	help_text = "Location",
        )
	
    Specific_Location = models.CharField(
	max_length = 50,
	blank = True,
	null = True,
	help_text = "Specific Location",
	)

    Running = models.BooleanField(
	help_text = "Running",
	)

    Chasing = models.BooleanField(
        help_text = "Chasing",
        )

    Climbing = models.BooleanField(
        help_text = "Climbing",
        )

    Eating = models.BooleanField(
        help_text = "Eating",
        )

    Foraging = models.BooleanField(
        help_text = "Foraging",
        )

    Other_Activities = models.CharField(
	max_length = 100,
	null = True,
	blank = True,
        help_text = "Other Activities"
        )

    Kuks = models.BooleanField(
        help_text = "Kuks",
        )

    Quaas = models.BooleanField(
        help_text = "Quaas",
        )

    Moans = models.BooleanField(
        help_text = "Moans",
        )

    Tail_flags = models.BooleanField(
        help_text = "Tail flags",
        )

    Tail_twitches = models.BooleanField(
        help_text = "Tail twitches",
        )

    Approaches = models.BooleanField(
        help_text = "Approaches",
        )

    Indifferent = models.BooleanField(
        help_text = "Indifferent",
        )

    Runs_from = models.BooleanField(
        help_text = "Runs from",
        )
 




