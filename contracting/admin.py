"""Admin configuration for general contracting service."""
from django.contrib import admin
from .models import ContractingOffering, ContractingProject


@admin.register(ContractingOffering)
class ContractingOfferingAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(ContractingProject)
class ContractingProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
