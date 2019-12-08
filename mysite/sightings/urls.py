from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns = [
	path('', views.list, name = 'list'),
	path('add/', views.add, name = 'add'),
	path('stats/', views.stats, name = 'stats'),
        path('<str:unique_id>/', views.update, name='update'),
	] 
