

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAdminQueryManagement', '0003_alter_querytype_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QueryType',
            new_name='QueryTypes',
        ),
    ]
