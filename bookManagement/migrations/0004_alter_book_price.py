

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0003_book_authordescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
