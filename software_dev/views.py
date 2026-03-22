"""Views for software development service."""
from django.shortcuts import render
from .models import DevOffering, DevProject


def index(request):
    """Software development service home page."""
    offerings = DevOffering.objects.all()
    projects = DevProject.objects.all()

    context = {
        'service_name': 'Software Development',
        'service_slug': 'software_dev',
        'service_icon': 'laptop-code',
        'offerings': offerings,
        'projects': projects,
    }

    return render(request, 'software_dev/index.html', context)
