"""Views for engineering service."""
from django.shortcuts import render
from .models import EngineeringOffering, EngineeringProject


def index(request):
    offerings = EngineeringOffering.objects.all()
    projects = EngineeringProject.objects.all()
    context = {
        'service_name': 'Engineering',
        'service_slug': 'engineering',
        'service_icon': 'wrench',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'engineering/index.html', context)
