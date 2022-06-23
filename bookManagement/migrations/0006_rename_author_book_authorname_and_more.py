

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0005_book_createdat_book_updatedat_alter_book_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authorName',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='bookDescription',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='file',
            new_name='bookFile',
        ),
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
    ]
