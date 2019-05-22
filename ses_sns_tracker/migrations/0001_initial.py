# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 11:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SESMailDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254)),
                ('message_id', models.CharField(max_length=128)),
                ('request_id', models.CharField(max_length=128)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Sent'), (1, 'Delivered'), (2, 'Bounced'), (3, 'Complaint')], default=0)),
                ('state_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Amazon SNS event data (bounce/complaint/delivery object)')),
                ('mail_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Amazon SNS mail data')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-updated_at',),
                'verbose_name': 'SES Mail Delivery',
                'verbose_name_plural': 'SES Mail Deliveries',
            },
        ),
    ]