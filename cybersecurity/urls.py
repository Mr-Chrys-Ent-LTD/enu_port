"""URL patterns for cybersecurity service."""
from django.urls import path
from . import views

app_name = 'cybersecurity'

urlpatterns = [
    path('', views.index, name='index'),
]
