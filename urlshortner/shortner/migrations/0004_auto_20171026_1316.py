# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_analyseurl_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyseurl',
            name='a_tag',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='analyseurl',
            name='abnormal_url',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='analyseurl',
            name='form_tag',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='analyseurl',
            name='google_index',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='analyseurl',
            name='using_mail',
            field=models.IntegerField(default=-1),
        ),
    ]
