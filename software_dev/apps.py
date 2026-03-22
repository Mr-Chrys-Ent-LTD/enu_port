"""App configuration for software development service."""
from django.apps import AppConfig


class SoftwareDevConfig(AppConfig):
    """Configuration class for the software development app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'software_dev'
    verbose_name = 'Software Development Services'
