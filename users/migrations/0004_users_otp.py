

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='otp',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
