

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('bannerId', models.AutoField(primary_key=True, serialize=False)),
                ('bannerImage', models.CharField(max_length=255)),
                ('IsActive', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'banners',
            },
        ),
    ]
