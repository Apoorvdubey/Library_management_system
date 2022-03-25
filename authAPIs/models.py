from django.db import models
from django.utils.timezone import now
# Create your models here.

class Banners(models.Model):
    bannerId = models.AutoField(primary_key=True)
    bannerImage = models.CharField(max_length=255)
    IsActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    class Meta:
        db_table='banners'