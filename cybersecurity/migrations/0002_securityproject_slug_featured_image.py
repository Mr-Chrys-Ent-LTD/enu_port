from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybersecurity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='securityproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/cybersecurity/'),
        ),
        migrations.AddField(
            model_name='securityproject',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
