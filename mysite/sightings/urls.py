from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns = [
	path('', views.list, name = 'list'),
        path('<str:unique_id>/', views.update, name='update'),
	path('add/', views.add.as_view(), name = 'add'),
	path('stats/', views.stats, name = 'stats'),
	] 
