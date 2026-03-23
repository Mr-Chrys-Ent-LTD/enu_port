from django.core.management.base import BaseCommand
from django.utils.text import slugify
from software_dev.models import DevProject
from logistics.models import LogisticsProject


class Command(BaseCommand):
    help = 'Update all project slugs'

    def handle(self, *args, **options):
        updated_count = 0

        # Update DevProject
        for project in DevProject.objects.all():
            if not project.slug or project.slug == '':
                project.slug = slugify(project.title)
                project.save()
                self.stdout.write(
                    f'Updated DevProject: {project.title} -> {project.slug}')
                updated_count += 1

        # Update LogisticsProject
        for project in LogisticsProject.objects.all():
            if not project.slug or project.slug == '':
                project.slug = slugify(project.title)
                project.save()
                self.stdout.write(
                    f'Updated LogisticsProject: {project.title} -> {project.slug}')
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Total projects updated: {updated_count}'))
