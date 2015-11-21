from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(datetime.now())
    class Meta:
        db_table = 'questions'
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField(max_length=200)
    class Meta:
        db_table = 'choices'
