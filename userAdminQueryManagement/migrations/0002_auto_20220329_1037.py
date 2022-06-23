

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userAdminQueryManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryType',
            fields=[
                ('queryTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'query_type',
            },
        ),
        migrations.AddField(
            model_name='useradminqueries',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useradminqueries',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useradminqueries',
            name='queryStatus',
            field=models.CharField(blank=True, choices=[('open', 'open'), ('inprogress', 'inprogress'), ('rejected', 'rejected'), ('closed', 'closed')], default='inprogress', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useradminqueries',
            name='queryTypeId',
            field=models.ForeignKey(blank=True, db_column='queryTypeId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='queryType', to='userAdminQueryManagement.querytype'),
        ),
    ]
