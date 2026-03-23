"""URL patterns for electrical and power service."""
from django.urls import path
from . import views

app_name = 'electrical_power'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug:project_slug>/',
         views.project_detail, name='project_detail'),
]
