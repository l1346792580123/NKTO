# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-05 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20171105_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nkto_user',
            name='signup_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
