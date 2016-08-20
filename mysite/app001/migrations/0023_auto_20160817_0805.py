# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0022_auto_20160817_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item004',
            name='field2',
            field=models.CharField(default='.', max_length=200, verbose_name='客戶'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field3',
            field=models.CharField(default='.', max_length=200, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field4',
            field=models.CharField(default='.', max_length=200, verbose_name='欠料量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field5',
            field=models.CharField(default='.', max_length=200, verbose_name='欠備庫量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field6',
            field=models.CharField(default='.', max_length=200, null=True, verbose_name='客訴量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field7',
            field=models.CharField(default='.', max_length=200, null=True, verbose_name='模具壽命'),
        ),
    ]