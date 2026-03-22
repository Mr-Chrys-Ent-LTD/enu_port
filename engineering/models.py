"""Models for engineering services."""
from django.db import models


class EngineeringOffering(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-wrench')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Engineering Offering'
        verbose_name_plural = 'Engineering Offerings'

    def __str__(self):
        return self.title


class EngineeringProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Engineering Project'
        verbose_name_plural = 'Engineering Projects'

    def __str__(self):
        return self.title
