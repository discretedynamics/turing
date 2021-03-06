# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0018_algorithm_new_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='new_version',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='A new version'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='status',
            field=models.CharField(default='pending', max_length=20, verbose_name='Algorithm Availability'),
        ),
    ]
