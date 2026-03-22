"""Models for logistics services."""
from django.db import models


class LogisticsOffering(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-boxes')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Logistics Offering'
        verbose_name_plural = 'Logistics Offerings'

    def __str__(self):
        return self.title


class LogisticsProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Logistics Project'
        verbose_name_plural = 'Logistics Projects'

    def __str__(self):
        return self.title
