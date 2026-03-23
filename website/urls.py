"""
URL patterns for the website app.
"""
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:project_slug>/',
         views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
