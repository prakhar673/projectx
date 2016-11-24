# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-22 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20161122_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='inception_year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 11, 22, 16, 19, 58, 625998)),
        ),
        migrations.AlterField(
            model_name='stream_master',
            name='stream_name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
