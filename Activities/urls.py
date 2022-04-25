from django.urls import path
from .views import activityDetail

app_name = 'Activities'

urlpatterns = [
    path('<slug>/',activityDetail, name="activity-detail"),
    ]