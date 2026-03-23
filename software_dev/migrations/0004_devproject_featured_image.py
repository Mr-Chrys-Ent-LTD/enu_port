from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_dev', '0003_populate_devproject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='devproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/software_dev/'),
        ),
    ]
