from django.shortcuts import render

from .models import Squirrel

from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

def list(request, *args, **kwargs):
    list = Squirrel.objects.all()
    fields = ['Unique_Squirrel_ID', 'Date']
    context = {'Squirrels': list, 'fields': fields, }
    return render(request, 'sightings/list.html', context)

def update(request, unique_id):
    return render(request, 'sightings/update.html')

class add(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')
    

def stats(request):
    list = Squirrel.objects.all()
    context = {'Squirrels': list }
    return render(request, 'sightings/stats.html')

      
# Create your views here.
