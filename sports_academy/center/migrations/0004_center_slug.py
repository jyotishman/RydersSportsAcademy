# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 19:22
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_auto_20190209_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='academy_name'),
        ),
    ]
