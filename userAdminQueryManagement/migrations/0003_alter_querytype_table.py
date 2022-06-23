

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAdminQueryManagement', '0002_auto_20220329_1037'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='querytype',
            table='query_types',
        ),
    ]
