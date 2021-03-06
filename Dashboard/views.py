from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from django.db.models import Sum

from CRM.models import Agent, Customer
from CRM.utils import pie_chart_gender_ratio, bar_chart_lead_customer_ratio, bar_chart_trend_category, Customer_Lead_By_Month
from Dashboard.models import Transaction
from .utils import transaction_line_graph

@staff_member_required
def dashboard(request):
    #Graphs
    #CRM GRAPHS
    context = pie_chart_gender_ratio()
    context.update(bar_chart_lead_customer_ratio())
    context.update(bar_chart_trend_category())
    context.update(Customer_Lead_By_Month())

    #Dashboard transaction GRAPH
    context.update(transaction_line_graph())
    
    #Logged in User Info
    user = Agent.objects.filter(agent=request.user)
    
    #Dashboard Attributes
    #CRM Customer Lead Total
    Customer_count = Customer.objects.filter(status='Customer').count()
    Lead_count = Customer.objects.filter(status='Lead').count()
    context.update({'user':user, 'Customer_count':Customer_count, 'Lead_count':Lead_count})

    #Montly Transactions
    thisMonth = datetime.now().month
    monthTransactions = Transaction.objects.filter(date_added__month=thisMonth)
    context.update({'monthTransactions':monthTransactions})

    #Credit and Debit
    monthlyCredit = Transaction.objects.filter(date_added__month=thisMonth, transaction='Credit').aggregate(Sum('amount'))
    monthlyDebit = Transaction.objects.filter(date_added__month=thisMonth, transaction='Debit').aggregate(Sum('amount'))
    context.update({'monthlyCredit':monthlyCredit, 'monthlyDebit':monthlyDebit})

    #Total Revenue and Expenditure (Yearly)
    thisYear = datetime.now().year
    yearlyCredit = Transaction.objects.filter(date_added__year=thisYear, transaction='Credit').aggregate(Sum('amount'))
    yearlyDebit = Transaction.objects.filter(date_added__year=thisYear, transaction='Debit').aggregate(Sum('amount'))
    context.update({'yearlyCredit':yearlyCredit, 'yearlyDebit':yearlyDebit})
    
    return render(request, "dashboard.html", context)


 