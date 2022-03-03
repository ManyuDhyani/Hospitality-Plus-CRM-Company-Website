from multiprocessing import context
from django.shortcuts import render
from CRM.utils import pie_chart_gender_ratio, bar_chart_lead_customer_ratio, bar_chart_trend_category, Customer_Lead_By_Month

def dashboard(request):
    context = pie_chart_gender_ratio()
    context.update(bar_chart_lead_customer_ratio())
    context.update(bar_chart_trend_category())
    context.update(Customer_Lead_By_Month())
    
    return render(request, "dashboard.html", context)


 