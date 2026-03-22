"""URL patterns for telecommunications service."""
from django.urls import path
from . import views

app_name = 'telecommunications'

urlpatterns = [
    path('', views.index, name='index'),
]
