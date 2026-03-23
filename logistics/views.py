"""Views for logistics service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import LogisticsOffering, LogisticsProject


def index(request):
    offerings = LogisticsOffering.objects.all()
    projects = LogisticsProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Logistics',
        'service_slug': 'logistics',
        'service_icon': 'boxes',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'logistics/index.html', context)


def project_detail(request, project_slug):
    project = get_object_or_404(LogisticsProject, slug=project_slug)
    context = {
        'service_name': 'Logistics',
        'project': project,
    }
    return render(request, 'logistics/project_detail.html', context)
