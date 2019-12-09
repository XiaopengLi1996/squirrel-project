from django.shortcuts import redirect
def welcome_page(request):
    return redirect('/sightings')
