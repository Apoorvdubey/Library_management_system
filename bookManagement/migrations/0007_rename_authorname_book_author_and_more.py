

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0006_rename_author_book_authorname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authorName',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bookDescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bookFile',
            new_name='file',
        ),
    ]
