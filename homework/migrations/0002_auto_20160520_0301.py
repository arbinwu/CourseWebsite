# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='content',
            field=models.FileField(upload_to='./files'),
        ),
    ]
