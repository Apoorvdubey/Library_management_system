from django.db import models
from django.utils.timezone import now
from users.models import Users
# Create your models here.

class Banners(models.Model):
    bannerId = models.AutoField(primary_key=True)
    bannerImage = models.CharField(max_length=255)
    IsActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    class Meta:
        db_table='banners'

class UserDonations(models.Model):
    paymentStatus = ((1,"pending"),(2,"completed"),(3,"canceled"),(4,"failed"))

    donationId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, related_name='userDonationDetail', db_column='userId')
    transactionId = models.CharField(max_length=255)
    payerId = models.CharField(max_length=255)
    payerEmail = models.CharField(max_length=255)
    paymentStatus = models.IntegerField(choices=paymentStatus,null=False,default=2)
    transactionMode = models.CharField(max_length=255)
    paymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    class Meta:
        db_table='user_donations'