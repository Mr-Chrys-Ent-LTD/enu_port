"""Views for electrical and power service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import ElectricalOffering, ElectricalProject

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
    """Electrical and power service home page."""
    offerings = ElectricalOffering.objects.all()
    projects = ElectricalProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Electrical & Power Solutions',
        'service_description': 'Comprehensive electrical and power solutions for businesses.',
        'offerings': offerings,
        'projects': projects,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'electrical_power/index.html', context)


def project_detail(request, project_slug):
    """Electrical and power project detail page."""
    project = get_object_or_404(ElectricalProject, slug=project_slug)
    offerings = ElectricalOffering.objects.all()

    context = {
        'service_name': 'Electrical & Power Solutions',
        'project': project,
        'offerings': offerings,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'electrical_power/project_detail.html', context)
