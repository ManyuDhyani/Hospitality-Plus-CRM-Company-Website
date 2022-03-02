from django.urls import path
from .views import landingLeadFormView, thankyou, pie_chart_category, pie_chart_gender, bar_chart_lead_customer_ratio

app_name = 'CRM'

urlpatterns = [
    path('book-your-spot/', landingLeadFormView.as_view(), name="Landing-Lead-Page"),
    path('success/', thankyou, name="Success"),
    path('pie-chart-category-attended/', pie_chart_category, name='pie-chart-category'),
    path('pie-chart-gender-ratio/', pie_chart_gender, name='pie-chart-gender'),
    path('bar-chart-lead-customer-ratio/', bar_chart_lead_customer_ratio, name='bar-chart-lead-customer-ratio'),
    ]