# Generated by Django 4.0.2 on 2022-04-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0022_alter_transaction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Refunds', 'Refunds'), ('Purchase', 'Purchase'), ('Miscellaneous', 'Miscellaneous'), ('IT and Maintenance', 'IT and Maintenance'), ('Sales', 'Sales'), ('Renting', 'Renting')], default='Miscellaneous', max_length=20),
        ),
    ]