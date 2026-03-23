from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineeringproject',
            name='featured_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='projects/engineering/'),
        ),
        migrations.AddField(
            model_name='engineeringproject',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
