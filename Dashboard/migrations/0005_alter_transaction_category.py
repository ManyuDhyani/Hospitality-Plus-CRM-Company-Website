# Generated by Django 4.0.2 on 2022-03-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_alter_transaction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Purchase', 'Purchase'), ('Renting', 'Renting'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Refunds', 'Refunds'), ('IT and Maintenance', 'IT and Maintenance'), ('Miscellaneous', 'Miscellaneous')], default='Miscellaneous', max_length=20),
        ),
    ]
