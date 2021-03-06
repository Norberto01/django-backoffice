# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20170201_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='expired_on',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='expired_month',
            field=models.CharField(blank=True, default='', max_length=2, verbose_name='Expired CC Month'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='expired_year',
            field=models.CharField(blank=True, default='', max_length=4, verbose_name='Expired CC Year'),
        ),
    ]
