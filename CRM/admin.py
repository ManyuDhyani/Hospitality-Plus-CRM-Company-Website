from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Agent)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'email']
    list_display_links = ['first_name']
    list_editable = ['last_name']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Customer, CustomerAdmin)
