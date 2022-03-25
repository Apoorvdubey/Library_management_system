from codecs import backslashreplace_errors
from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Book(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    bookCover = models.CharField(max_length=255, default=None, null=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    authorDescription = models.TextField(null=True)
    description = models.TextField()
    price= models.IntegerField(null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    file = models.CharField(max_length=255, default=None, null=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'books'
    