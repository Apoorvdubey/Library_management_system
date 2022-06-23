

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdminQueries',
            fields=[
                ('userAdminQueryId', models.AutoField(primary_key=True, serialize=False)),
                ('queryStatus', models.CharField(blank=True, choices=[('open', 'open'), ('inprogress', 'inprogress'), ('rejected', 'rejected'), ('closed', 'closed')], default='open', max_length=255, null=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('lastMessageSetDateTime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('adminId', models.ForeignKey(blank=True, db_column='adminId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('userId', models.ForeignKey(blank=True, db_column='userId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_admin_queries',
            },
        ),
        migrations.CreateModel(
            name='UserAdminQueriesContents',
            fields=[
                ('queryContentId', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('isSentByAdmin', models.BooleanField(default=False)),
                ('isRead', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('userAdminQueryId', models.ForeignKey(blank=True, db_column='userAdminQueryId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='queryDetail', to='userAdminQueryManagement.useradminqueries')),
            ],
            options={
                'db_table': 'user_admin_queries_content',
            },
        ),
    ]
