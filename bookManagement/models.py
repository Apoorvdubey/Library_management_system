from codecs import backslashreplace_errors
from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models
from django.utils.timezone import now
from users.models import Users

# Create your models here.

class Book(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    bookCover = models.CharField(max_length=255, default=None, null=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    authorDescription = models.TextField(null=True)
    description = models.TextField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    file = models.CharField(max_length=255, default=None, null=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'books'

class UserBookmarkBook(models.Model):
  
    bookmarkId = models.AutoField(primary_key=True)
    bookmarkStatus = models.BooleanField(default=False)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, related_name='userDetail', db_column='userId')
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE, default=None, blank=True, related_name='bookDetail', db_column='bookId')
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    class Meta:
        db_table='user_bookmark_books'

class UserBookReadingStatus(models.Model):
  
    bookReadingStatusId = models.AutoField(primary_key=True)
    bookReadingStatus = models.BooleanField(default=False)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, blank=True, related_name='readingUserDetail', db_column='userId')
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE, default=None, blank=True, related_name='readingBookDetail', db_column='bookId')
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    class Meta:
        db_table='user_book_reading_status'
    