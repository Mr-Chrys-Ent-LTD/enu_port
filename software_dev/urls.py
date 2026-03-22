"""URL patterns for software development service."""
from django.urls import path
from . import views

app_name = 'software_dev'

urlpatterns = [
    path('', views.index, name='index'),
]
