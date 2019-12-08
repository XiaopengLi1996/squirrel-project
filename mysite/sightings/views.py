from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Squirrel
from .forms import getFormforSightings
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

def list(request, *args, **kwargs):
    list_ = Squirrel.objects.all()
    fields = ['Unique_Squirrel_ID', 'Date']
    context = {'squirrels': list_, 'fields': fields, }
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
    if request.method == 'POST':
        form = getFormforSightings(request.POST)
        if form.is_valid():
            a = form['Unique_Squirrel_ID'].value()
            sighting = form.save(commit=False)
            sighting.save()
            return redirect(f'/sightings/{a}')
    else:
        form = getFormforSightings()
    context ={
        'form':form,
    }
    return render(request, 'sightings/add.html', context)
    

def stats(request):
    list1 = Squirrel.objects.all()
    context = {
        'squirrels': list1 
    }
    return render(request, 'sightings/stats.html', context)

      
# Create your views here.
