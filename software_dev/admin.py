"""Admin configuration for software development service."""
from django.contrib import admin
from .models import DevOffering, DevProject


@admin.register(DevOffering)
class DevOfferingAdmin(admin.ModelAdmin):
    """Admin interface for development offerings."""

    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(DevProject)
class DevProjectAdmin(admin.ModelAdmin):
    """Admin interface for development projects."""

    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description', 'technologies']
    list_editable = ['order']
