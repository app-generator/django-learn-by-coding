from django.db import models

# Create your models here.

class Book(models.Model):                                 # <- NEW
    title            = models.CharField(max_length=100)   # <- NEW 
    author           = models.CharField(max_length=100)   # <- NEW
    publication_date = models.DateField()                 # <- NEW
