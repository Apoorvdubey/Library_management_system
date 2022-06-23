

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookManagement', '0010_alter_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImages',
            fields=[
                ('bookImageId', models.AutoField(primary_key=True, serialize=False)),
                ('bookImage', models.CharField(default=None, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('bookId', models.ForeignKey(blank=True, db_column='bookId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fetchingBookDetail', to='bookManagement.book')),
            ],
            options={
                'db_table': 'book_images',
            },
        ),
    ]
