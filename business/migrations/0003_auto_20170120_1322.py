# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20170112_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='payment_id',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='related_transaction_id',
            new_name='related_transaction',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='service_id',
            new_name='service',
        ),
    ]
