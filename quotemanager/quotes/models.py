from django.db import models

# Create your models here.
class Quote(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quote = models.TextField(unique=True)
    speaker = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)


