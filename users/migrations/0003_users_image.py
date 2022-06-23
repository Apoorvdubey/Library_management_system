
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_gender_alter_users_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
