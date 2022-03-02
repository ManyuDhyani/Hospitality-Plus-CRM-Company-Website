from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

from import_export.admin import ImportExportModelAdmin
from .resources import CustomerResource

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Agent)
admin.site.register(Newsletter)


class CustomerAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resources_class = CustomerResource
    list_display = ['first_name', 'last_name', 'age', 'gender', 'phone_number', 'email', 'status', 'date_added']
    list_display_links = ['first_name']
    #list_editable = ['email', 'phone_number']
    list_filter = ['agent', 'status', 'category_attended']
    search_fields = ['first_name', 'last_name', 'email']
    exclude = ('changed_by',)
    date_hierarchy = 'date_added'
    save_on_top = True

admin.site.register(Customer, CustomerAdmin)
