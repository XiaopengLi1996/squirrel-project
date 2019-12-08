from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Squirrel
from .forms import getFormforSightings

def list(request):
    list_ = Squirrel.objects.all()
    fields = ['Links by Squirrel ID', 'longitude', 'Latitude', 'Age', 'Date']
    context = {
	'squirrels': list_, 
	'fields': fields,
	 }
    return render(request, 'sightings/list.html', context)

def update(request, unique_id):
    obj = get_object_or_404(Squirrel, Unique_Squirrel_ID = unique_id)
    form = getFormforSightings(request.POST or None, instance = obj) 
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/{unique_id}')
    context ={
        'form':form,
        'squirrel_id':unique_id,
    }
    return render(request, 'sightings/update.html', context)

def add(request): 
    form = getFormforSightings(request.POST)
    if form.is_valid():
        a = form['Unique_Squirrel_ID'].value()
        sighting = form.save(commit=False)
        sighting.save()
        return redirect(f'/sightings/{a}')
    context ={
	'form':form
	}    
    return render(request, 'sightings/add.html', context)
    

def stats(request):
    context ={
	'counts': Squirrel.objects.count(),
	'jun_counts': Squirrel.objects.filter(Age='Juvenile').count(),
	'adt_counts': Squirrel.objects.filter(Age='Adult').count(),
	'black_counts': Squirrel.objects.filter(Primary_Fur_Color='Black').count(),
	'gray_counts': Squirrel.objects.filter(Primary_Fur_Color='Gray').count(),
	'cin_counts': Squirrel.objects.filter(Primary_Fur_Color='Cinnammon').count(),
	'eat_counts': Squirrel.objects.filter(Eating=True).count(),
	'run_counts': Squirrel.objects.filter(Running=True).count(),
	}

    return render(request, 'sightings/stats.html', context)

      
