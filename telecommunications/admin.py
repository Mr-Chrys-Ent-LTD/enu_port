"""Admin configuration for telecommunications service."""
from django.contrib import admin
from .models import TelecomOffering, TelecomProject


@admin.register(TelecomOffering)
class TelecomOfferingAdmin(admin.ModelAdmin):
    """Admin interface for telecom offerings."""

    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(TelecomProject)
class TelecomProjectAdmin(admin.ModelAdmin):
    """Admin interface for telecom projects."""

    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
