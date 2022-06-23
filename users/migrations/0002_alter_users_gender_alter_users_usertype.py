

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'others')], default='M', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='userType',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=255),
        ),
    ]
