# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0002_likeanswer_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeanswer',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
