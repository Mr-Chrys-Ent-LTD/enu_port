"""Views for logistics service."""
from django.shortcuts import render
from .models import LogisticsOffering, LogisticsProject


def index(request):
    offerings = LogisticsOffering.objects.all()
    projects = LogisticsProject.objects.all()
    context = {
        'service_name': 'Logistics',
        'service_slug': 'logistics',
        'service_icon': 'boxes',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'logistics/index.html', context)
