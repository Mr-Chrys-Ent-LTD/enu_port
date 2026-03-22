"""App configuration for telecommunications service."""
from django.apps import AppConfig


class TelecommunicationsConfig(AppConfig):
    """Configuration class for the telecommunications app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telecommunications'
    verbose_name = 'Telecommunications Services'
