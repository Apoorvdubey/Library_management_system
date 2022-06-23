

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0002_book_author_book_isavailable_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authorDescription',
            field=models.TextField(null=True),
        ),
    ]
