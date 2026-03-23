from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    DevProject = apps.get_model('software_dev', 'DevProject')
    for project in DevProject.objects.all():
        if not project.slug:
            project.slug = slugify(project.title)
            project.save(update_fields=['slug'])


def populate_logistics_slugs(apps, schema_editor):
    LogisticsProject = apps.get_model('logistics', 'LogisticsProject')
    for project in LogisticsProject.objects.all():
        if not project.slug:
            project.slug = slugify(project.title)
            project.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('software_dev', '0002_devproject_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
