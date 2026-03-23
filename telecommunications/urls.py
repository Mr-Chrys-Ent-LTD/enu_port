"""URL patterns for telecommunications service."""
from django.urls import path
from . import views

app_name = 'telecommunications'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug:project_slug>/',
         views.project_detail, name='project_detail'),
]
