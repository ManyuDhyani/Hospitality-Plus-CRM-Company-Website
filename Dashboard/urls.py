from django.urls import path
from .views import dashboard

app_name = 'Dashboard'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard')
    ]