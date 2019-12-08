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
    obj = get_object_or_404(Squirrel, Unique_Squirrel_ID = unique_id)
    form = getFormforSightings(request.POST or None, instance = obj) 
    if form.is_valid()
        form.save()
        return redirect(f'/sightings/{unique_id}')
    context ={
        'form':form
        'squirrel_id':unique_id,
    }
    return render(request, 'sightings/update.html', context)

class add(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')
    

def stats(request):
    list = Squirrel.objects.all()
    context = {
        'Squirrels': list 
    }
    return render(request, 'sightings/stats.html', context)

      
# Create your views here.
