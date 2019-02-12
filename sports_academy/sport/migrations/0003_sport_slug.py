# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 19:22
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20190206_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
    ]