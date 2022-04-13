# Generated by Django 4.0.2 on 2022-04-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_alter_transaction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Purchase', 'Purchase'), ('Marketing', 'Marketing'), ('Refunds', 'Refunds'), ('Renting', 'Renting'), ('Sales', 'Sales'), ('Miscellaneous', 'Miscellaneous'), ('IT and Maintenance', 'IT and Maintenance')], default='Miscellaneous', max_length=20),
        ),
    ]