from codecs import backslashreplace_errors
from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models

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
    