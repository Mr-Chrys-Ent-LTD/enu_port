from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractingproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/contracting/'),
        ),
        migrations.AddField(
            model_name='contractingproject',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
