# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-14 02:08
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='description',
        ),
        migrations.RemoveField(
            model_name='brands',
            name='priority',
        ),
        migrations.AddField(
            model_name='brands',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='brands',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='brands',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
