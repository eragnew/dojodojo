# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-22 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('manufacturer', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]