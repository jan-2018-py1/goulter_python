# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20180216_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]