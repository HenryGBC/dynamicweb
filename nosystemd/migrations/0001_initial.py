# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 06:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0002_billingaddress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last4', models.CharField(max_length=4)),
                ('cc_brand', models.CharField(max_length=10)),
                ('stripe_charge_id', models.CharField(max_length=100, null=True)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.BillingAddress')),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
