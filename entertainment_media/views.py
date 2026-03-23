"""Views for entertainment and media service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import EntertainmentOffering, EntertainmentProject

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
    """Entertainment and media service home page."""
    offerings = EntertainmentOffering.objects.all()
    projects = EntertainmentProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Entertainment & Media Solutions',
        'service_description': 'Creative entertainment and media production services.',
        'offerings': offerings,
        'projects': projects,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'entertainment_media/index.html', context)


def project_detail(request, project_slug):
    """Entertainment and media project detail page."""
    project = get_object_or_404(EntertainmentProject, slug=project_slug)
    offerings = EntertainmentOffering.objects.all()

    context = {
        'service_name': 'Entertainment & Media Solutions',
        'project': project,
        'offerings': offerings,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'entertainment_media/project_detail.html', context)
