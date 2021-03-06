# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-20 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_billingaddress'),
        ('membership', '0006_auto_20160526_0445'),
        ('digitalglarus', '0007_auto_20160820_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiporder',
            name='billing_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utils.BillingAddress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membershiporder',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='membership.StripeCustomer'),
            preserve_default=False,
        ),
    ]
