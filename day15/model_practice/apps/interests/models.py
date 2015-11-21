from __future__ import unicode_literals
from django.db import models

class Interest(models.Model):
    name = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'interests'

class User(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    occupation = models.TextField(max_length=200)
    interest = models.ForeignKey(Interest)
    class User:
        db_table = 'users'
