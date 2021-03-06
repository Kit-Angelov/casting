# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0002_auto_20171115_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='rating',
        ),
        migrations.AddField(
            model_name='employee',
            name='human_rating',
            field=models.FloatField(default=1, verbose_name='Рейтинг человеческих качеств'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='professional_rating',
            field=models.FloatField(default=2, verbose_name='Рейтинг проф навыков'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='human_skills',
            field=models.IntegerField(choices=[(1, '1'), (3, '3'), (5, '5'), (4, '4'), (2, '2')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='professional_skills',
            field=models.IntegerField(choices=[(1, '1'), (3, '3'), (5, '5'), (4, '4'), (2, '2')]),
        ),
    ]
