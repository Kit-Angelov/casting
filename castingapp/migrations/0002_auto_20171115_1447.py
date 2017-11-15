# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('castingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional_skills', models.IntegerField(choices=[(4, '4'), (5, '5'), (2, '2'), (1, '1'), (3, '3')])),
                ('human_skills', models.IntegerField(choices=[(4, '4'), (5, '5'), (2, '2'), (1, '1'), (3, '3')])),
                ('comments', models.TextField(blank=True, max_length=1000, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='castingapp.Employer')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='rating',
            field=models.FloatField(default=1, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]