# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0012_auto_20171126_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='type',
        ),
        migrations.AlterField(
            model_name='review',
            name='human_skills',
            field=models.IntegerField(choices=[(3, '3'), (1, '1'), (2, '2'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='professional_skills',
            field=models.IntegerField(choices=[(3, '3'), (1, '1'), (2, '2'), (4, '4'), (5, '5')]),
        ),
    ]
