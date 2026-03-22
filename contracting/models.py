"""Models for general contracting services."""
from django.db import models


class ContractingOffering(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-building')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Contracting Offering'
        verbose_name_plural = 'Contracting Offerings'

    def __str__(self):
        return self.title


class ContractingProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Contracting Project'
        verbose_name_plural = 'Contracting Projects'

    def __str__(self):
        return self.title
