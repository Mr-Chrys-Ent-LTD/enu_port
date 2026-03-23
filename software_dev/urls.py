"""URL patterns for software development service."""
from django.urls import path
from . import views

app_name = 'software_dev'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug:project_slug>/',
         views.project_detail, name='project_detail'),
]
