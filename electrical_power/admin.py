"""Admin configuration for electrical and power service."""
from django.contrib import admin
from .models import ElectricalOffering, ElectricalProject


@admin.register(ElectricalOffering)
class ElectricalOfferingAdmin(admin.ModelAdmin):
    """Admin interface for electrical offerings."""

    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(ElectricalProject)
class ElectricalProjectAdmin(admin.ModelAdmin):
    """Admin interface for electrical projects."""

    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
