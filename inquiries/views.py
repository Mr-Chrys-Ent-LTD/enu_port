"""Views for handling service inquiries."""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import ServiceInquiry
from .forms import ServiceInquiryForm


@require_http_methods(["GET", "POST"])
def submit_inquiry(request, service=None):
    """
    Handle inquiry submission for a specific service.

    Args:
        request: HTTP request object
        service: Service identifier (optional, can also come from POST data)

    Returns:
        Renders form or redirects on success
    """
    if request.method == 'POST':
        form = ServiceInquiryForm(request.POST)

        # Get service from POST data or URL parameter
        service_value = request.POST.get('service') or service

        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.service = service_value
            inquiry.save()

            messages.success(
                request,
                'Thank you for your inquiry! We will get back to you shortly.'
            )

            # If AJAX request, return JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'message': 'Inquiry submitted successfully!'
                })

            # Redirect to service page or home
            return redirect(f'/{service}/' if service else '/')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'error',
                    'errors': form.errors
                }, status=400)
    else:
        form = ServiceInquiryForm()

    context = {
        'form': form,
        'service': service,
    }

    return render(request, 'inquiries/inquiry_form.html', context)


def inquiry_list(request):
    """List all inquiries (admin view)."""
    inquiries = ServiceInquiry.objects.all()

    # Filter by service if specified
    service_filter = request.GET.get('service')
    if service_filter:
        inquiries = inquiries.filter(service=service_filter)

    # Filter by read status
    read_filter = request.GET.get('read')
    if read_filter == 'unread':
        inquiries = inquiries.filter(is_read=False)
    elif read_filter == 'read':
        inquiries = inquiries.filter(is_read=True)

    context = {
        'inquiries': inquiries,
        'service_filter': service_filter,
        'read_filter': read_filter,
    }

    return render(request, 'inquiries/inquiry_list.html', context)


def inquiry_detail(request, pk):
    """View details of a specific inquiry."""
    try:
        inquiry = ServiceInquiry.objects.get(pk=pk)
        if not inquiry.is_read:
            inquiry.is_read = True
            inquiry.save()
    except ServiceInquiry.DoesNotExist:
        return redirect('inquiry_list')

    context = {'inquiry': inquiry}
    return render(request, 'inquiries/inquiry_detail.html', context)
