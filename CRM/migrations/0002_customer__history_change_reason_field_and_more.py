# Generated by Django 4.0.2 on 2022-02-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='_history_change_reason_field',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='_history_change_reason_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
