# Generated by Django 4.0.2 on 2022-04-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0008_alter_activities_altitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='altitude',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='activities',
            name='difficulty',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='activities',
            name='distance',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='activities',
            name='duration_days',
            field=models.CharField(default='', max_length=20),
        ),
    ]