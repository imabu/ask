# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/avatar.png', upload_to='avatars'),
            preserve_default=False,
        ),
    ]