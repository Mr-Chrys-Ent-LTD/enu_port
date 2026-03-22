"""Admin configuration for cybersecurity service."""
from django.contrib import admin
from .models import SecurityOffering, SecurityProject


@admin.register(SecurityOffering)
class SecurityOfferingAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(SecurityProject)
class SecurityProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
