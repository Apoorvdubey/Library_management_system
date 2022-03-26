from django.db import models
from users.models import Users
from django.utils.timezone import now
# Create your models here.


class UserAdminQueries(models.Model):
    QUERY_STATUS = (("open", "open"), ('inprogress', 'inprogress'), ('rejected', 'rejected'), ('closed', 'closed'))

    userAdminQueryId = models.AutoField(primary_key=True)
    queryStatus = models.CharField(max_length=255, choices=QUERY_STATUS, default='open', blank=True, null=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, related_name='user', db_column='userId')
    adminId = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, related_name='admin', db_column='adminId')
    createdAt = models.DateTimeField(default=now, editable=False)
    lastMessageSetDateTime = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table='user_admin_queries'


class UserAdminQueriesContents(models.Model):

    queryContentId = models.AutoField(primary_key=True)
    message = models.TextField()
    isSentByAdmin = models.BooleanField(default=False)
    isRead = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    userAdminQueryId = models.ForeignKey(UserAdminQueries, on_delete=models.CASCADE, default=None, blank=True, related_name='queryDetail', db_column='userAdminQueryId')
    
    class Meta:
        db_table = 'user_admin_queries_content'