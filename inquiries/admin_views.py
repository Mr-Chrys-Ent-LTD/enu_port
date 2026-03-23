"""Custom admin views for managing inquiries and contact messages."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from website.models import ContactMessage, Project
from website.forms import ContactForm, ProjectForm
from .models import ServiceInquiry
from .forms import (
    ServiceInquiryForm,
    SecurityProjectForm,
    TelecomProjectForm,
    DevProjectForm,
    EngineeringProjectForm,
    LogisticsProjectForm,
    ContractingProjectForm,
    ElectricalProjectForm,
    EntertainmentProjectForm,
    TrainingProjectForm
)
from cybersecurity.models import SecurityProject
from telecommunications.models import TelecomProject
from software_dev.models import DevProject
from engineering.models import EngineeringProject
from logistics.models import LogisticsProject
from contracting.models import ContractingProject
from electrical_power.models import ElectricalProject
from entertainment_media.models import EntertainmentProject
from training_consulting.models import TrainingProject


def is_admin(user):
    """Check if user is a superuser or staff."""
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    """Dashboard showing all enquiries and contact messages."""
    # Get filter parameters
    inquiry_filter = request.GET.get('inquiry_filter', 'all')
    contact_filter = request.GET.get('contact_filter', 'all')
    search = request.GET.get('search', '').strip()

    # Get all inquiries and contact messages
    inquiries = ServiceInquiry.objects.all()
    contact_messages = ContactMessage.objects.all()

    # Filter inquiries
    if inquiry_filter == 'unread':
        inquiries = inquiries.filter(is_read=False)
    elif inquiry_filter == 'responded':
        inquiries = inquiries.filter(is_responded=True)
    elif inquiry_filter == 'pending':
        inquiries = inquiries.filter(is_responded=False)

    # Filter contact messages
    if contact_filter == 'unread':
        contact_messages = contact_messages.filter(is_read=False)

    # Search
    if search:
        inquiries = inquiries.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(company__icontains=search) |
            Q(subject__icontains=search)
        )
        contact_messages = contact_messages.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(message__icontains=search)
        )

    # Count stats
    stats = {
        'total_inquiries': ServiceInquiry.objects.count(),
        'unread_inquiries': ServiceInquiry.objects.filter(is_read=False).count(),
        'pending_inquiries': ServiceInquiry.objects.filter(is_responded=False).count(),
        'total_messages': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
    }

    context = {
        'inquiries': inquiries[:50],  # Paginate to 50 items
        'contact_messages': contact_messages[:50],
        'stats': stats,
        'search': search,
        'inquiry_filter': inquiry_filter,
        'contact_filter': contact_filter,
    }

    return render(request, 'inquiries/admin_dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def inquiry_detail(request, inquiry_id):
    """View and respond to a specific inquiry."""
    inquiry = get_object_or_404(ServiceInquiry, id=inquiry_id)

    if request.method == 'POST':
        response_message = request.POST.get('response_message', '').strip()
        send_response = request.POST.get('send_response')

        if response_message and send_response:
            try:
                # Send email response
                send_mail(
                    subject=f'Re: {inquiry.subject}',
                    message=response_message,
                    from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@mrchrys.com',
                    recipient_list=[inquiry.email],
                    fail_silently=False,
                )

                # Mark as responded
                inquiry.is_responded = True
                inquiry.is_read = True
                inquiry.save()

                messages.success(
                    request, f'Response sent to {inquiry.name} successfully!')
                return redirect('inquiries:admin_dashboard')
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')

        # Mark as read even if just viewed
        if not inquiry.is_read:
            inquiry.is_read = True
            inquiry.save()

    context = {
        'inquiry': inquiry,
    }
    return render(request, 'inquiries/inquiry_detail.html', context)


@login_required
@user_passes_test(is_admin)
def contact_message_detail(request, message_id):
    """View and respond to a specific contact message."""
    contact_msg = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        response_message = request.POST.get('response_message', '').strip()
        send_response = request.POST.get('send_response')

        if response_message and send_response:
            try:
                # Send email response
                send_mail(
                    subject=f'Re: Your Message from {contact_msg.name}',
                    message=response_message,
                    from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@mrchrys.com',
                    recipient_list=[contact_msg.email],
                    fail_silently=False,
                )

                # Mark as read
                contact_msg.is_read = True
                contact_msg.save()

                messages.success(
                    request, f'Response sent to {contact_msg.name} successfully!')
                return redirect('inquiries:admin_dashboard')
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')

        # Mark as read even if just viewed
        if not contact_msg.is_read:
            contact_msg.is_read = True
            contact_msg.save()

    context = {
        'message': contact_msg,
    }
    return render(request, 'inquiries/contact_message_detail.html', context)


@login_required
@user_passes_test(is_admin)
@require_http_methods(["POST"])
def mark_as_read(request, inquiry_id):
    """Mark an inquiry as read."""
    inquiry = get_object_or_404(ServiceInquiry, id=inquiry_id)
    inquiry.is_read = True
    inquiry.save()
    messages.success(request, 'Marked as read.')
    return redirect('inquiries:inquiry_detail', inquiry_id=inquiry_id)


@login_required
@user_passes_test(is_admin)
@require_http_methods(["POST"])
def delete_inquiry(request, inquiry_id):
    """Delete an inquiry."""
    inquiry = get_object_or_404(ServiceInquiry, id=inquiry_id)
    inquiry.delete()
    messages.success(request, 'Inquiry deleted successfully.')
    return redirect('inquiries:admin_dashboard')


@login_required
@user_passes_test(is_admin)
@require_http_methods(["POST"])
def delete_contact_message(request, message_id):
    """Delete a contact message."""
    contact_msg = get_object_or_404(ContactMessage, id=message_id)
    contact_msg.delete()
    messages.success(request, 'Contact message deleted successfully.')
    return redirect('inquiries:admin_dashboard')


@login_required
@user_passes_test(is_admin)
def create_inquiry(request):
    """Create a new service inquiry from admin panel."""
    if request.method == 'POST':
        form = ServiceInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            messages.success(
                request, f'Service inquiry from {inquiry.name} created successfully!')
            return redirect('inquiries:inquiry_detail', inquiry_id=inquiry.id)
    else:
        form = ServiceInquiryForm()

    context = {
        'form': form,
        'title': 'Create Service Inquiry',
        'button_text': 'Create Inquiry',
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
def create_contact_message(request):
    """Create a new contact message from admin panel."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            messages.success(
                request, f'Contact message from {message.name} created successfully!')
            return redirect('inquiries:contact_message_detail', message_id=message.id)
    else:
        form = ContactForm()

    context = {
        'form': form,
        'title': 'Create Contact Message',
        'button_text': 'Create Message',
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
def edit_inquiry(request, inquiry_id):
    """Edit an existing service inquiry."""
    inquiry = get_object_or_404(ServiceInquiry, id=inquiry_id)

    if request.method == 'POST':
        form = ServiceInquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service inquiry updated successfully!')
            return redirect('inquiries:inquiry_detail', inquiry_id=inquiry.id)
    else:
        form = ServiceInquiryForm(instance=inquiry)

    context = {
        'form': form,
        'title': 'Edit Service Inquiry',
        'button_text': 'Update Inquiry',
        'inquiry': inquiry,
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
def edit_contact_message(request, message_id):
    """Edit an existing contact message."""
    contact_msg = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact_msg)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact message updated successfully!')
            return redirect('inquiries:contact_message_detail', message_id=contact_msg.id)
    else:
        form = ContactForm(instance=contact_msg)

    context = {
        'form': form,
        'title': 'Edit Contact Message',
        'button_text': 'Update Message',
        'message': contact_msg,
    }
    return render(request, 'inquiries/create_form.html', context)


# ==================== PROJECT MANAGEMENT ====================

@login_required
@user_passes_test(is_admin)
def projects_list(request):
    """View all projects with management options."""
    projects = Project.objects.all().order_by('-completion_date')

    context = {
        'projects': projects,
    }
    return render(request, 'inquiries/projects_list.html', context)


@login_required
@user_passes_test(is_admin)
def create_project(request):
    """Create a new project from admin panel."""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(
                request, f'Project "{project.title}" created successfully!')
            return redirect('inquiries:project_detail', project_id=project.id)
    else:
        form = ProjectForm()

    context = {
        'form': form,
        'title': 'Create Project',
        'button_text': 'Create Project',
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
def project_detail(request, project_id):
    """View project details."""
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project': project,
    }
    return render(request, 'inquiries/project_detail.html', context)


@login_required
@user_passes_test(is_admin)
def edit_project(request, project_id):
    """Edit an existing project."""
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('inquiries:project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'title': 'Edit Project',
        'button_text': 'Update Project',
        'project': project,
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
@require_http_methods(["POST"])
def delete_project(request, project_id):
    """Delete a project."""
    project = get_object_or_404(Project, id=project_id)
    project_title = project.title
    project.delete()
    messages.success(
        request, f'Project "{project_title}" deleted successfully.')
    return redirect('inquiries:projects_list')


# ==================== SERVICE-SPECIFIC PROJECT MANAGEMENT ====================

@login_required
@user_passes_test(is_admin)
def service_projects_list(request):
    """View all service-specific projects across all services."""
    # Collect all projects from all services
    security_projects = SecurityProject.objects.all()
    telecom_projects = TelecomProject.objects.all()
    dev_projects = DevProject.objects.all()
    engineering_projects = EngineeringProject.objects.all()
    logistics_projects = LogisticsProject.objects.all()
    contracting_projects = ContractingProject.objects.all()
    electrical_projects = ElectricalProject.objects.all()
    entertainment_projects = EntertainmentProject.objects.all()
    training_projects = TrainingProject.objects.all()

    # Combine all into a single list with service info
    all_projects = []

    for project in security_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Cybersecurity',
            'service_slug': 'cybersecurity',
            'model_name': 'securityproject'
        })

    for project in telecom_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Telecommunications',
            'service_slug': 'telecommunications',
            'model_name': 'telecomproject'
        })

    for project in dev_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Software Development',
            'service_slug': 'software_dev',
            'model_name': 'devproject'
        })

    for project in engineering_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Engineering',
            'service_slug': 'engineering',
            'model_name': 'engineeringproject'
        })

    for project in logistics_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Logistics',
            'service_slug': 'logistics',
            'model_name': 'logisticsproject'
        })

    for project in contracting_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Contracting',
            'service_slug': 'contracting',
            'model_name': 'contractingproject'
        })

    for project in electrical_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Electrical & Power',
            'service_slug': 'electrical_power',
            'model_name': 'electricalproject'
        })

    for project in entertainment_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Entertainment & Media',
            'service_slug': 'entertainment_media',
            'model_name': 'entertainmentproject'
        })

    for project in training_projects:
        all_projects.append({
            'id': project.id,
            'title': project.title,
            'client': project.client,
            'completion_date': project.completion_date,
            'service': 'Training & Consulting',
            'service_slug': 'training_consulting',
            'model_name': 'trainingproject'
        })

    # Sort by completion date (newest first)
    all_projects.sort(key=lambda x: x['completion_date'] if x['completion_date'] else '',
                      reverse=True)

    context = {
        'projects': all_projects,
    }
    return render(request, 'inquiries/service_projects_list.html', context)


@login_required
@user_passes_test(is_admin)
def create_service_project(request):
    """Create a service-specific project with service selection."""
    service_type = request.GET.get('service', '').lower()

    # Map service types to forms
    form_map = {
        'cybersecurity': SecurityProjectForm,
        'telecommunications': TelecomProjectForm,
        'software_dev': DevProjectForm,
        'engineering': EngineeringProjectForm,
        'logistics': LogisticsProjectForm,
        'contracting': ContractingProjectForm,
        'electrical_power': ElectricalProjectForm,
        'entertainment_media': EntertainmentProjectForm,
        'training_consulting': TrainingProjectForm,
    }

    # If no service selected, show selection page
    if request.method == 'GET' and not service_type:
        services = [
            {'name': 'Cybersecurity', 'slug': 'cybersecurity', 'icon': '🔒'},
            {'name': 'Telecommunications', 'slug': 'telecommunications', 'icon': '📡'},
            {'name': 'Software Development', 'slug': 'software_dev', 'icon': '💻'},
            {'name': 'Engineering', 'slug': 'engineering', 'icon': '⚙️'},
            {'name': 'Logistics', 'slug': 'logistics', 'icon': '📦'},
            {'name': 'Contracting', 'slug': 'contracting', 'icon': '🏗️'},
            {'name': 'Electrical & Power', 'slug': 'electrical_power', 'icon': '⚡'},
            {'name': 'Entertainment & Media',
                'slug': 'entertainment_media', 'icon': '🎬'},
            {'name': 'Training & Consulting',
                'slug': 'training_consulting', 'icon': '📚'},
        ]
        context = {
            'services': services,
            'title': 'Select Service Type',
        }
        return render(request, 'inquiries/select_service.html', context)

    # Get the form class for the selected service
    if service_type not in form_map:
        messages.error(request, 'Invalid service type selected.')
        return redirect('inquiries:create_service_project')

    FormClass = form_map[service_type]

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(
                request, f'Project "{project.title}" created successfully in {service_type.replace("_", " ").title()}!')
            return redirect('inquiries:service_projects_list')
    else:
        form = FormClass()

    context = {
        'form': form,
        'title': f'Create {service_type.replace("_", " ").title()} Project',
        'button_text': 'Create Project',
        'service_type': service_type,
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
def edit_service_project(request, service_type, project_id):
    """Edit a service-specific project."""
    service_type = service_type.lower()

    # Map service types to models and forms
    model_map = {
        'cybersecurity': SecurityProject,
        'telecommunications': TelecomProject,
        'software_dev': DevProject,
        'engineering': EngineeringProject,
        'logistics': LogisticsProject,
        'contracting': ContractingProject,
        'electrical_power': ElectricalProject,
        'entertainment_media': EntertainmentProject,
        'training_consulting': TrainingProject,
    }

    form_map = {
        'cybersecurity': SecurityProjectForm,
        'telecommunications': TelecomProjectForm,
        'software_dev': DevProjectForm,
        'engineering': EngineeringProjectForm,
        'logistics': LogisticsProjectForm,
        'contracting': ContractingProjectForm,
        'electrical_power': ElectricalProjectForm,
        'entertainment_media': EntertainmentProjectForm,
        'training_consulting': TrainingProjectForm,
    }

    if service_type not in model_map:
        messages.error(request, 'Invalid service type.')
        return redirect('inquiries:service_projects_list')

    Model = model_map[service_type]
    FormClass = form_map[service_type]
    project = get_object_or_404(Model, id=project_id)

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('inquiries:service_projects_list')
    else:
        form = FormClass(instance=project)

    context = {
        'form': form,
        'title': f'Edit Project',
        'button_text': 'Update Project',
        'project': project,
        'service_type': service_type,
    }
    return render(request, 'inquiries/create_form.html', context)


@login_required
@user_passes_test(is_admin)
@require_http_methods(["POST"])
def delete_service_project(request, service_type, project_id):
    """Delete a service-specific project."""
    service_type = service_type.lower()

    # Map service types to models
    model_map = {
        'cybersecurity': SecurityProject,
        'telecommunications': TelecomProject,
        'software_dev': DevProject,
        'engineering': EngineeringProject,
        'logistics': LogisticsProject,
        'contracting': ContractingProject,
        'electrical_power': ElectricalProject,
        'entertainment_media': EntertainmentProject,
        'training_consulting': TrainingProject,
    }

    if service_type not in model_map:
        messages.error(request, 'Invalid service type.')
        return redirect('inquiries:service_projects_list')

    Model = model_map[service_type]
    project = get_object_or_404(Model, id=project_id)
    project_title = project.title
    project.delete()

    messages.success(
        request, f'Project "{project_title}" deleted successfully.')
    return redirect('inquiries:service_projects_list')
