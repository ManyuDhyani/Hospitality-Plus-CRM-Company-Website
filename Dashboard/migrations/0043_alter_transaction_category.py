# Generated by Django 4.0.2 on 2022-06-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0042_alter_transaction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('IT and Maintenance', 'IT and Maintenance'), ('Purchase', 'Purchase'), ('Renting', 'Renting'), ('Refunds', 'Refunds'), ('Miscellaneous', 'Miscellaneous'), ('Marketing', 'Marketing'), ('Sales', 'Sales')], default='Miscellaneous', max_length=20),
        ),
    ]
