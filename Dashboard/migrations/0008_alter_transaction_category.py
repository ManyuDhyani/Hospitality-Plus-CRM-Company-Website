# Generated by Django 4.0.2 on 2022-03-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_alter_transaction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Refunds', 'Refunds'), ('Renting', 'Renting'), ('IT and Maintenance', 'IT and Maintenance'), ('Miscellaneous', 'Miscellaneous'), ('Sales', 'Sales'), ('Purchase', 'Purchase'), ('Marketing', 'Marketing')], default='Miscellaneous', max_length=20),
        ),
    ]
