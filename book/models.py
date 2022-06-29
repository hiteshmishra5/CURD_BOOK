from django.db import models

# Create your models here.

class Book(models.Model):
    isbn_number = models.CharField(max_length = 100)
    book_name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)

