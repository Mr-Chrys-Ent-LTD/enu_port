from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telecommunications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telecomproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/telecommunications/'),
        ),
        migrations.AddField(
            model_name='telecomproject',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
