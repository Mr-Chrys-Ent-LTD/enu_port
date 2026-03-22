"""Views for cybersecurity service."""
from django.shortcuts import render
from .models import SecurityOffering, SecurityProject


def index(request):
    offerings = SecurityOffering.objects.all()
    projects = SecurityProject.objects.all()
    context = {
        'service_name': 'Cybersecurity',
        'service_slug': 'cybersecurity',
        'service_icon': 'shield-alt',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'cybersecurity/index.html', context)
