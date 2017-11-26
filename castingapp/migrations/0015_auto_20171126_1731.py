# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0014_auto_20171126_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casting',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='castingapp.Employer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='human_skills',
            field=models.IntegerField(choices=[(1, '1'), (4, '4'), (3, '3'), (2, '2'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='professional_skills',
            field=models.IntegerField(choices=[(1, '1'), (4, '4'), (3, '3'), (2, '2'), (5, '5')]),
        ),
    ]