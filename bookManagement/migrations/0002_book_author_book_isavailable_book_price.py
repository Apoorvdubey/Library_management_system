

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
