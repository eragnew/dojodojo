from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.FloatField()
    class Meta:
        db_table = 'products'

class Cart(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'carts'

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    class Meta:
        db_table = 'cartproducts'
