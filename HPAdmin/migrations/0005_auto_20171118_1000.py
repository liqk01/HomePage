# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HPAdmin', '0004_auto_20171118_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relopermissions',
            name='DoManage',
        ),
        migrations.RemoveField(
            model_name='domanage',
            name='Relopermissions',
        ),
        migrations.AddField(
            model_name='domanage',
            name='Permissions',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Relopermissions',
        ),
    ]
