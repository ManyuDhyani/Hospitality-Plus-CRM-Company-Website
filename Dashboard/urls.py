from django.urls import path
from .views import dashboard

app_name = 'Dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard')
    ]