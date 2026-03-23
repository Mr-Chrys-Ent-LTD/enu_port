"""URL patterns for training and consulting service."""
from django.urls import path
from . import views

app_name = 'training_consulting'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug:project_slug>/',
         views.project_detail, name='project_detail'),
]
