# Generated by Django 4.0.2 on 2022-03-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_alter_transaction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Purchase', 'Purchase'), ('Renting', 'Renting'), ('Refunds', 'Refunds'), ('IT and Maintenance', 'IT and Maintenance'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Miscellaneous', 'Miscellaneous')], default='Miscellaneous', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction',
            field=models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=6),
        ),
    ]