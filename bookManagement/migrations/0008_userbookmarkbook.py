

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookManagement', '0007_rename_authorname_book_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookmarkBook',
            fields=[
                ('bookmarkId', models.AutoField(primary_key=True, serialize=False)),
                ('bookmarkStatus', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('bookId', models.ForeignKey(blank=True, db_column='bookId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookDetail', to='bookManagement.book')),
                ('userId', models.ForeignKey(blank=True, db_column='userId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userDetail', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_bookmark_books',
            },
        ),
    ]
