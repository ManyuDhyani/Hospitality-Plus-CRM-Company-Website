import imp
from django.contrib import admin
from .models import ActivitiesCategories, Activities

admin.site.register(ActivitiesCategories)
admin.site.register(Activities)