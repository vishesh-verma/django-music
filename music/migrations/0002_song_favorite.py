# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]