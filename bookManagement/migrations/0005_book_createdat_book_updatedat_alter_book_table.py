

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='book',
            name='updatedAt',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
