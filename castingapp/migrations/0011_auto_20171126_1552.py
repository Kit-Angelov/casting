# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0010_auto_20171126_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casting',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='human_skills',
            field=models.IntegerField(choices=[(4, '4'), (2, '2'), (5, '5'), (1, '1'), (3, '3')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='professional_skills',
            field=models.IntegerField(choices=[(4, '4'), (2, '2'), (5, '5'), (1, '1'), (3, '3')]),
        ),
    ]