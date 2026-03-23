from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_populate_logisticsproject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticsproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/logistics/'),
        ),
    ]
