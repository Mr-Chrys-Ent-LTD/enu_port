"""Admin configuration for training and consulting service."""
from django.contrib import admin
from .models import TrainingOffering, TrainingProject


@admin.register(TrainingOffering)
class TrainingOfferingAdmin(admin.ModelAdmin):
    """Admin interface for training offerings."""

    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']


@admin.register(TrainingProject)
class TrainingProjectAdmin(admin.ModelAdmin):
    """Admin interface for training projects."""

    list_display = ['title', 'client', 'completion_date', 'order']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    list_editable = ['order']
