"""Views for engineering service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import EngineeringOffering, EngineeringProject


def index(request):
    offerings = EngineeringOffering.objects.all()
    projects = EngineeringProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Engineering',
        'service_slug': 'engineering',
        'service_icon': 'wrench',
        'offerings': offerings,
        'projects': projects,
    }
    return render(request, 'engineering/index.html', context)


def project_detail(request, project_slug):
    """Engineering project detail page."""
    project = get_object_or_404(EngineeringProject, slug=project_slug)
    context = {
        'service_name': 'Engineering',
        'project': project,
    }
    return render(request, 'engineering/project_detail.html', context)
