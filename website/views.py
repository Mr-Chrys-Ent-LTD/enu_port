"""
Views for MRCHRYS ENT NIG LTD website.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Service, Project
from .forms import ContactForm


# Company Information Dictionary
COMPANY_INFO = {
    'name': 'MrChrys',
    'tagline': 'Building Smart Solutions Across Technology, Telecom, Engineering & Beyond',
    'email': 'info@mrchrys.com',
    'phone': '+2347012224108',
    'whatsapp': '+2347012224108',
    'address': 'Abuja, Nigeria',
    'vision': "To become a leading multi-industry solutions provider in Africa, recognized for our innovation, reliability, and commitment to customer success.",
    'mission': "To deliver high-quality, innovative, and reliable services that empower businesses and communities to thrive in a competitive and rapidly evolving global marketplace",
    'values': ['Integrity', 'Excellence', 'Innovation', 'Reliability', 'Customer Satisfaction'],
}

# Mapping of service categories to service apps
SERVICE_APPS = {
    'Telecommunications': {
        'name': 'Telecommunications',
        'url': '/telecommunications/',
        'icon': 'fas fa-tower-cell',
        'description': 'Network design, installation, and maintenance services'
    },
    'Software & IT': {
        'name': 'Software Development',
        'url': '/software-dev/',
        'icon': 'fas fa-code',
        'description': 'Custom software solutions and development services'
    },
    'Cybersecurity': {
        'name': 'Cybersecurity',
        'url': '/cybersecurity/',
        'icon': 'fas fa-shield-alt',
        'description': 'Security audits, testing, and threat monitoring'
    },
    'Engineering & Construction': {
        'name': 'Engineering',
        'url': '/engineering/',
        'icon': 'fas fa-hard-hat',
        'description': 'Engineering consulting and implementation services'
    },
    'Logistics & Supply': {
        'name': 'Logistics',
        'url': '/logistics/',
        'icon': 'fas fa-truck',
        'description': 'Supply chain and logistics management'
    },
    'General Contracts': {
        'name': 'General Contracting',
        'url': '/contracting/',
        'icon': 'fas fa-handshake',
        'description': 'Professional contracting and project management'
    },
}

# Services data structure
SERVICES_DATA = {
    'Telecommunications': [
        'Telecom site installation and maintenance',
        'Fiber optic installation',
        'Network optimization',
        'Equipment installation',
    ],
    'Software & IT': [
        'Web development',
        'Mobile apps',
        'Enterprise software',
        'Cloud services',
    ],
    'Cybersecurity': [
        'Network security',
        'Penetration testing',
        'Security audits',
        'Threat monitoring',
    ],
    'Engineering & Construction': [
        'Building construction',
        'Civil engineering',
        'Facility maintenance',
    ],
    'Electrical & Power': [
        'Solar installation',
        'Inverter systems',
        'Electrical wiring',
    ],
    'Logistics & Supply': [
        'Procurement',
        'Import/export',
        'Transportation',
    ],
    'General Contracts': [
        'Corporate contracts',
        'Office equipment supply',
        'Industrial materials',
    ],
    'Entertainment & Media': [
        'Event management',
        'Media production',
        'Content creation',
    ],
    'Training & Consulting': [
        'ICT training',
        'Cybersecurity awareness',
        'Business consulting',
    ],
    'Data & Smart Systems': [
        'Data analytics',
        'Smart systems',
        'Digital transformation',
    ],
}

# Icons for services
SERVICE_ICONS = {
    'Telecommunications': 'fas fa-tower-cell',
    'Software & IT': 'fas fa-code',
    'Cybersecurity': 'fas fa-shield-alt',
    'Engineering & Construction': 'fas fa-hard-hat',
    'Electrical & Power': 'fas fa-bolt',
    'Logistics & Supply': 'fas fa-truck',
    'General Contracts': 'fas fa-handshake',
    'Entertainment & Media': 'fas fa-film',
    'Training & Consulting': 'fas fa-chalkboard-user',
    'Data & Smart Systems': 'fas fa-chart-bar',
}


def home(request):
    """View for the home page."""
    context = {
        'company': COMPANY_INFO,
        'services': SERVICES_DATA,
        'service_icons': SERVICE_ICONS,
    }
    return render(request, 'website/home.html', context)


def about(request):
    """View for the about page."""
    context = {
        'company': COMPANY_INFO,
    }
    return render(request, 'website/about.html', context)


def services(request):
    """View for the services page."""
    context = {
        'company': COMPANY_INFO,
        'services': SERVICES_DATA,
        'service_icons': SERVICE_ICONS,
    }
    return render(request, 'website/services.html', context)


def projects(request):
    """View for the projects page."""
    # Get projects from database
    projects_list = Project.objects.all()

    context = {
        'company': COMPANY_INFO,
        'projects': projects_list,
    }
    return render(request, 'website/projects.html', context)


def project_detail(request, project_slug):
    """View for displaying individual project details."""
    project = get_object_or_404(Project, slug=project_slug)

    # Get related projects (same category)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(slug=project_slug)[:3]

    context = {
        'company': COMPANY_INFO,
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'website/project_detail.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """View for the contact page and form submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()

            # Send email notification (optional - configure in production)
            try:
                send_mail(
                    subject=f'New Contact Message from {contact_message.name}',
                    message=f'Name: {contact_message.name}\nEmail: {contact_message.email}\nPhone: {contact_message.phone}\n\nMessage:\n{contact_message.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@mrchrys.com',
                    recipient_list=['info@mrchrys.com'],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            messages.success(
                request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('website:contact')
    else:
        form = ContactForm()

    context = {
        'company': COMPANY_INFO,
        'form': form,
    }
    return render(request, 'website/contact.html', context)
