

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authAPIs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDonations',
            fields=[
                ('donationId', models.AutoField(primary_key=True, serialize=False)),
                ('transactionId', models.CharField(max_length=255)),
                ('payerId', models.CharField(max_length=255)),
                ('payerEmail', models.CharField(max_length=255)),
                ('paymentStatus', models.IntegerField(choices=[(1, 'pending'), (2, 'completed'), (3, 'canceled'), (4, 'rejected')], default=2)),
                ('transactionMode', models.CharField(max_length=255)),
                ('paymentAmount', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('userId', models.ForeignKey(blank=True, db_column='userId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userDonationDetail', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_donations',
            },
        ),
    ]
