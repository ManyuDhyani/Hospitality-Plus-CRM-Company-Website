from django.urls import path
from .views import activityDetail, activitiesView

app_name = 'Activities'

urlpatterns = [
    path('', activitiesView.as_view(), name="activities"),
    path('<slug>/',activityDetail, name="activity-detail"),
    ]