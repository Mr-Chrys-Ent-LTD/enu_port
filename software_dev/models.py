"""Models for software development services."""
from django.db import models
from django.utils.text import slugify


class DevOffering(models.Model):
    """Model for software development service offerings."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-code')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Development Offering'
        verbose_name_plural = 'Development Offerings'

    def __str__(self):
        return self.title


class DevProject(models.Model):
    """Model for software development projects."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True, null=True)
    technologies = models.CharField(max_length=300, blank=True, null=True)
    featured_image = models.ImageField(
        upload_to='projects/software_dev/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', 'order']
        verbose_name = 'Development Project'
        verbose_name_plural = 'Development Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
