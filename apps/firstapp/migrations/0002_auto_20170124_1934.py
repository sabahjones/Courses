# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
