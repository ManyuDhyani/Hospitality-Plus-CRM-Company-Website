from multiprocessing import context
from django.shortcuts import render
from CRM.utils import pie_chart_gender_ratio, bar_chart_lead_customer_ratio

def dashboard(request):
    context = pie_chart_gender_ratio()
    context.update(bar_chart_lead_customer_ratio())
    # print(context)
    return render(request, "dashboard.html", context)


 