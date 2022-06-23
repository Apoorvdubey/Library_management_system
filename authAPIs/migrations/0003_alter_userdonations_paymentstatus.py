

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAPIs', '0002_userdonations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdonations',
            name='paymentStatus',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'completed'), (3, 'canceled'), (4, 'failed')], default=2),
        ),
    ]
