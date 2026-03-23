"""Views for general contracting service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import ContractingOffering, ContractingProject


def index(request):
    offerings = ContractingOffering.objects.all()
    projects = ContractingProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'General Contracting',
        'service_slug': 'contracting',
        'service_icon': 'building',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'contracting/index.html', context)


def project_detail(request, project_slug):
    """General contracting project detail page."""
    project = get_object_or_404(ContractingProject, slug=project_slug)
    context = {
        'service_name': 'General Contracting',
        'project': project,
    }
    return render(request, 'contracting/project_detail.html', context)
