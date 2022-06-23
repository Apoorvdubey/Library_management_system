

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='isEmailVerified',
            field=models.BooleanField(default=False),
        ),
    ]
