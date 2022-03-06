from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['amount', 'description', 'category', 'transaction', 'date_added', 'date_modified']
    list_filter = ['transaction', 'category']
    date_hierarchy = 'date_added'

admin.site.register(Transaction, TransactionAdmin)