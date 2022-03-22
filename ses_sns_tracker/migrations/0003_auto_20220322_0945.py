# Generated by Django 3.2.12 on 2022-03-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ses_sns_tracker', '0002_alter_sesmaildelivery_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesmaildelivery',
            name='mail_data',
            field=models.JSONField(blank=True, default=dict, help_text='Amazon SNS mail data'),
        ),
        migrations.AlterField(
            model_name='sesmaildelivery',
            name='state_data',
            field=models.JSONField(blank=True, default=dict, help_text='Amazon SNS event data (bounce/complaint/delivery object)'),
        ),
    ]