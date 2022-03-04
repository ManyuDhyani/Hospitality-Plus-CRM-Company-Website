from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from CRM.utils import pie_chart_gender_ratio, bar_chart_lead_customer_ratio, bar_chart_trend_category, Customer_Lead_By_Month, user_profile_picture


@staff_member_required
def dashboard(request):
    context = pie_chart_gender_ratio()
    context.update(bar_chart_lead_customer_ratio())
    context.update(bar_chart_trend_category())
    context.update(Customer_Lead_By_Month())


    context.update(user_profile_picture(request.user))
    
    
    return render(request, "dashboard.html", context)


 