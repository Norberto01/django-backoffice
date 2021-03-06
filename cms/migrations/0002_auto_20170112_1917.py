# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0002_auto_20170112_1917'),
        ('customer', '0001_initial'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagechannel',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_page', to='customer.Channel', verbose_name='Service Channel'),
        ),
        migrations.AddField(
            model_name='pagechannel',
            name='post',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_channel_page', to='cms.Prepyme'),
        ),
        migrations.AddField(
            model_name='amountnode',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount_channel', to='customer.Channel', verbose_name='Service Channel'),
        ),
        migrations.AddField(
            model_name='amountnode',
            name='channel_amount',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_channel_amounts', to='business.ChannelAmounts'),
        ),
        migrations.AlterUniqueTogether(
            name='prepyrendition',
            unique_together=set([('image', 'filter_spec', 'focal_point_key')]),
        ),
    ]
