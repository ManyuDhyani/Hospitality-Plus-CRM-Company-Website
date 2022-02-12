from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Category)
admin.site.register(Agent)

class CustomerAdmin(SimpleHistoryAdmin):
    list_display = ['first_name', 'last_name', 'age', 'phone_number', 'email', 'date_added']
    list_display_links = ['first_name']
    list_editable = ['email', 'phone_number']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name', 'email']
    exclude = ('changed_by',)

admin.site.register(Customer, CustomerAdmin)
