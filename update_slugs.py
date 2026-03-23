from django.utils.text import slugify
from logistics.models import LogisticsProject
from software_dev.models import DevProject
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrchrys_project.settings')
django.setup()


# Update DevProject
updated_count = 0
for project in DevProject.objects.all():
    if not project.slug or project.slug == '':
        project.slug = slugify(project.title)
        project.save()
        print(f'Updated DevProject: {project.title} -> {project.slug}')
        updated_count += 1

# Update LogisticsProject
for project in LogisticsProject.objects.all():
    if not project.slug or project.slug == '':
        project.slug = slugify(project.title)
        project.save()
        print(f'Updated LogisticsProject: {project.title} -> {project.slug}')
        updated_count += 1

print(f'Total projects updated: {updated_count}')
