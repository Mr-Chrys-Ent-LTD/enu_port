"""Views for software development service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import DevOffering, DevProject


def index(request):
    """Software development service home page."""
    offerings = DevOffering.objects.all()
    projects = DevProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Software Development',
        'service_slug': 'software_dev',
        'service_icon': 'laptop-code',
        'offerings': offerings,
        'projects': projects,
    }

    return render(request, 'software_dev/index.html', context)


def project_detail(request, project_slug):
    """Software development project detail page."""
    project = get_object_or_404(DevProject, slug=project_slug)

    # Split technologies by comma if they exist
    technologies_list = []
    if project.technologies:
        technologies_list = [tech.strip()
                             for tech in project.technologies.split(',')]

    context = {
        'service_name': 'Software Development',
        'project': project,
        'technologies_list': technologies_list,
    }
    return render(request, 'software_dev/project_detail.html', context)
