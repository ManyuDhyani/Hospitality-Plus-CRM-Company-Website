# Generated by Django 4.0.2 on 2022-04-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_alter_blogs_options_alter_contactdetails_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
