from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200)
    manufacturer = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'products'
