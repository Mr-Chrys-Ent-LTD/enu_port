"""App configuration for contracting service."""
from django.apps import AppConfig


class ContractingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contracting'
    verbose_name = 'General Contracting Services'
