"""Admin configuration for engineering service."""
from django.contrib import admin
from .models import EngineeringOffering, EngineeringProject


@admin.register(EngineeringOffering)
class EngineeringOfferingAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(EngineeringProject)
class EngineeringProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
