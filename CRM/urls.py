from django.urls import path
from .views import landing

app_name = 'CRM'

urlpatterns = [
    path('book-your-spot/', landing),
    ]