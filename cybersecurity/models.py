"""Models for cybersecurity services."""
from django.db import models


class SecurityOffering(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-shield-alt')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Security Offering'
        verbose_name_plural = 'Security Offerings'

    def __str__(self):
        return self.title


class SecurityProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Security Project'
        verbose_name_plural = 'Security Projects'

    def __str__(self):
        return self.title
