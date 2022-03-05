from cProfile import label
from django.db import models

TRANSACTION_CHOICES = {
    ('Credit', 'Credit'),
    ('Debit', 'Debit')
}

class Transaction(models.Model):
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    transaction = models.CharField(choices=TRANSACTION_CHOICES, max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)