# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_remove_answer_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_id_no',
            field=models.IntegerField(default=None),
        ),
    ]