from cProfile import label
from unicodedata import category
from django.db import models

TRANSACTION_CHOICES = {
    ('Credit', 'Credit'),
    ('Debit', 'Debit')
}
TRANSACTION_CATEGORY_CHOICES = {
    ('Purchase', 'Purchase'),
    ('Renting', 'Renting'),
    ('Sales', 'Sales'),
    ('Marketing', 'Marketing'),
    ('IT and Maintenance', 'IT and Maintenance'),
    ('Refunds', 'Refunds'),
    ('Miscellaneous', 'Miscellaneous')
}
class Transaction(models.Model):
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=TRANSACTION_CATEGORY_CHOICES, default='Miscellaneous')
    transaction = models.CharField(choices=TRANSACTION_CHOICES, max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)