# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-22 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='full_name',
        ),
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='middle_name',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='middle_name'),
        ),
    ]
