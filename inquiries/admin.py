"""Admin configuration for inquiries app."""
from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceInquiry


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    """Admin interface for managing service inquiries."""

    list_display = [
        'name',
        'service_display',
        'email',
        'subject',
        'status_display',
        'created_at',
    ]
    list_filter = ['service', 'is_read', 'is_responded', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message', 'company']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Inquiry Information', {
            'fields': ('service', 'name', 'email', 'phone', 'company')
        }),
        ('Inquiry Content', {
            'fields': ('subject', 'message')
        }),
        ('Project Details', {
            'fields': ('budget', 'timeline'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_read', 'is_responded')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_read', 'mark_as_unread', 'mark_as_responded']

    def service_display(self, obj):
        """Display service with icon."""
        service_emoji = {
            'telecommunications': '📡',
            'software_dev': '💻',
            'cybersecurity': '🔒',
            'engineering': '⚙️',
            'logistics': '📦',
            'contracting': '🏗️',
        }
        emoji = service_emoji.get(obj.service, '')
        return f"{emoji} {obj.get_service_display()}"

    service_display.short_description = 'Service'

    def status_display(self, obj):
        """Display status with color."""
        if obj.is_responded:
            color = 'green'
            status = 'Responded'
        elif obj.is_read:
            color = 'orange'
            status = 'Read'
        else:
            color = 'red'
            status = 'New'

        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            status
        )

    status_display.short_description = 'Status'

    def mark_as_read(self, request, queryset):
        """Mark inquiries as read."""
        count = queryset.update(is_read=True)
        self.message_user(request, f'{count} inquiry(ies) marked as read.')

    mark_as_read.short_description = 'Mark selected as read'

    def mark_as_unread(self, request, queryset):
        """Mark inquiries as unread."""
        count = queryset.update(is_read=False)
        self.message_user(request, f'{count} inquiry(ies) marked as unread.')

    mark_as_unread.short_description = 'Mark selected as unread'

    def mark_as_responded(self, request, queryset):
        """Mark inquiries as responded."""
        count = queryset.update(is_responded=True)
        self.message_user(
            request, f'{count} inquiry(ies) marked as responded.')

    mark_as_responded.short_description = 'Mark selected as responded'
