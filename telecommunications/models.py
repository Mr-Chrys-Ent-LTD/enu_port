"""Models for telecommunications services."""
from django.db import models
from django.utils.text import slugify


class TelecomOffering(models.Model):
    """Model for telecommunications service offerings."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-tower-mobile')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Telecom Offering'
        verbose_name_plural = 'Telecom Offerings'

    def __str__(self):
        return self.title


class TelecomProject(models.Model):
    """Model for telecommunications projects."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    featured_image = models.ImageField(
        upload_to='projects/telecommunications/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Telecom Project'
        verbose_name_plural = 'Telecom Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
