"""Views for cybersecurity service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import SecurityOffering, SecurityProject


def index(request):
    offerings = SecurityOffering.objects.all()
    projects = SecurityProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Cybersecurity',
        'service_slug': 'cybersecurity',
        'service_icon': 'shield-alt',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'cybersecurity/index.html', context)


def project_detail(request, project_slug):
    """Cybersecurity project detail page."""
    project = get_object_or_404(SecurityProject, slug=project_slug)
    context = {
        'service_name': 'Cybersecurity',
        'project': project,
    }
    return render(request, 'cybersecurity/project_detail.html', context)
