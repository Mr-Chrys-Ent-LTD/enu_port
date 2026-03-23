"""Views for telecommunications service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import TelecomOffering, TelecomProject

COMPANY_INFO = {
    'name': 'MrChrys',
    'tagline': 'Building Smart Solutions Across Technology, Telecom, Engineering & Beyond',
    'email': 'info@mrchrys.com',
    'phone': '+2347012224108',
    'whatsapp': '+2347012224108',
    'address': 'Abuja, Nigeria',
    'vision': 'To become a leading multi-industry solutions provider in Africa.',
    'mission': 'To deliver high-quality, innovative, and reliable services that empower businesses and communities.',
    'values': ['Integrity', 'Excellence', 'Innovation', 'Reliability', 'Customer Satisfaction'],
}


def index(request):
    """Telecommunications service home page."""
    offerings = TelecomOffering.objects.all()
    projects = TelecomProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Telecommunications',
        'service_slug': 'telecommunications',
        'service_icon': 'tower-mobile',
        'company': COMPANY_INFO,
        'offerings': offerings,
        'projects': projects,
    }

    return render(request, 'telecommunications/index.html', context)


def project_detail(request, project_slug):
    """Telecommunications project detail page."""
    project = get_object_or_404(TelecomProject, slug=project_slug)
    context = {
        'service_name': 'Telecommunications',
        'project': project,
    }
    return render(request, 'telecommunications/project_detail.html', context)
