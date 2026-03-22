"""App configuration for the inquiries module."""
from django.apps import AppConfig


class InquiriesConfig(AppConfig):
    """Configuration class for the inquiries app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inquiries'
    verbose_name = 'Service Inquiries'
