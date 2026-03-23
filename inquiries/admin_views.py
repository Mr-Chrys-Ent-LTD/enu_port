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
from .forms import ServiceInquiryForm


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
