# Generated by Django 4.0.2 on 2022-04-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0010_alter_transaction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Purchase', 'Purchase'), ('IT and Maintenance', 'IT and Maintenance'), ('Refunds', 'Refunds'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Miscellaneous', 'Miscellaneous'), ('Renting', 'Renting')], default='Miscellaneous', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=6),
        ),
    ]
