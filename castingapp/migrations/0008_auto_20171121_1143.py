# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0007_auto_20171119_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='human_skills',
            field=models.IntegerField(choices=[(3, '3'), (5, '5'), (4, '4'), (2, '2'), (1, '1')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='professional_skills',
            field=models.IntegerField(choices=[(3, '3'), (5, '5'), (4, '4'), (2, '2'), (1, '1')]),
        ),
    ]