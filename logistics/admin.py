"""Admin configuration for logistics service."""
from django.contrib import admin
from .models import LogisticsOffering, LogisticsProject


@admin.register(LogisticsOffering)
class LogisticsOfferingAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(LogisticsProject)
class LogisticsProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
