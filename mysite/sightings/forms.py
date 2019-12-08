from django import forms
from .models import Squirrel

class getFormforSightings(forms.ModelForm): 
    class Meta:
        model = Squirrel
        all_fields = [i.name for i in Squirrel._meta.get_fields()]
        fields = []
        fields.extend(all_fields)
