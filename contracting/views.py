"""Views for general contracting service."""
from django.shortcuts import render
from .models import ContractingOffering, ContractingProject


def index(request):
    offerings = ContractingOffering.objects.all()
    projects = ContractingProject.objects.all()
    context = {
        'service_name': 'General Contracting',
        'service_slug': 'contracting',
        'service_icon': 'building',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'contracting/index.html', context)
