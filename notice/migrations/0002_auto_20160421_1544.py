# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['time']},
        ),
    ]
