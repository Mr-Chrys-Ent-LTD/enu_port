"""Models for service inquiries across all service apps."""
from django.db import models


class ServiceInquiry(models.Model):
    """Model for storing service inquiries from any service app."""

    SERVICE_CHOICES = (
        ('telecommunications', 'Telecommunications'),
        ('software_dev', 'Software Development'),
        ('cybersecurity', 'Cybersecurity'),
        ('engineering', 'Engineering'),
        ('logistics', 'Logistics'),
        ('contracting', 'General Contracting'),
    )

    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    budget = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Optional budget range"
    )
    timeline = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Expected timeline"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    is_responded = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Service Inquiry'
        verbose_name_plural = 'Service Inquiries'
        indexes = [
            models.Index(fields=['service', '-created_at']),
            models.Index(fields=['is_read']),
        ]

    def __str__(self):
        return f"{self.get_service_display()} - {self.name} ({self.created_at.strftime('%Y-%m-%d')})"
