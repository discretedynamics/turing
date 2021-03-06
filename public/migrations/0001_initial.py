# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Algorithm Name')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('description', models.TextField(verbose_name='Description')),
                ('website', models.URLField(verbose_name='Website')),
                ('docker_image', models.TextField(verbose_name='Docker Image')),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Author Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('personal_website', models.URLField(verbose_name='Personal Website')),
                ('organization', models.TextField(verbose_name='Organization')),
                ('organization_website', models.URLField(verbose_name='Organization Website')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Paper Title')),
                ('url', models.URLField(verbose_name='Link')),
            ],
        ),
    ]
