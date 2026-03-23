"""Admin configuration for entertainment and media service."""
from django.contrib import admin
from .models import EntertainmentOffering, EntertainmentProject


@admin.register(EntertainmentOffering)
class EntertainmentOfferingAdmin(admin.ModelAdmin):
    """Admin interface for entertainment offerings."""

    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(EntertainmentProject)
class EntertainmentProjectAdmin(admin.ModelAdmin):
    """Admin interface for entertainment projects."""

    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
