# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-22 10:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20161122_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='inception_year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 11, 22, 16, 12, 44, 181199)),
        ),
        migrations.AlterField(
            model_name='stream_master',
            name='stream_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
