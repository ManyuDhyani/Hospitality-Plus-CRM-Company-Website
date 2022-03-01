from django.urls import path
from .views import landingLeadFormView, thankyou, dashboard

app_name = 'CRM'

urlpatterns = [
    path('book-your-spot/', landingLeadFormView.as_view(), name="Landing-Lead-Page"),
    path('success/', thankyou, name="Success"),
    ]