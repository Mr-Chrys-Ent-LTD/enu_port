"""Views for training and consulting service."""
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import TrainingOffering, TrainingProject

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
    """Training and consulting service home page."""
    offerings = TrainingOffering.objects.all()
    projects = TrainingProject.objects.all()

    # Ensure all projects have slugs
    for project in projects:
        if not project.slug:
            project.slug = slugify(project.title)
            project.save()

    context = {
        'service_name': 'Training & Consulting Solutions',
        'service_description': 'Professional training and consulting services for businesses.',
        'offerings': offerings,
        'projects': projects,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'training_consulting/index.html', context)


def project_detail(request, project_slug):
    """Training and consulting project detail page."""
    project = get_object_or_404(TrainingProject, slug=project_slug)
    offerings = TrainingOffering.objects.all()

    context = {
        'service_name': 'Training & Consulting Solutions',
        'project': project,
        'offerings': offerings,
        'company_info': COMPANY_INFO,
    }
    return render(request, 'training_consulting/project_detail.html', context)
