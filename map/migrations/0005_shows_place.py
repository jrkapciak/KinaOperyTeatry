# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20171123_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='map.Place'),
        ),
    ]
