from .models import Customer, Agent
from django.db.models import Count
import calendar

def pie_chart_gender_ratio():
    labels = []
    data = []
    context = {}

    queryset = Customer.objects.values('gender').annotate(gender_ratio=Count('gender')).order_by('gender_ratio')

    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)

    context = {
        'labelsGender': labels,
        'dataGender': data,
    }

    return context

def bar_chart_lead_customer_ratio():
    labels = []
    data = []
    context = {}

    queryset = Customer.objects.values('status').annotate(lead_customer_ratio=Count('status')).order_by('lead_customer_ratio')

    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)

    context = {
        'labelsLeadCustomer': labels,
        'dataLeadCustomer': data,
    }

    return context


def bar_chart_trend_category():
    labels = []
    data = []
    context = {}

    queryset = Customer.objects.values('category_attended__title').annotate(trend_count=Count('category_attended__title')).order_by('-trend_count')[:7]
    
    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)
        
    context = {
        'labelsTrendCategories': labels,
        'dataTrendCategories': data,
    }

    return context


def Customer_Lead_By_Month():
    labelsCustomer = []
    dataCustomer = []
    labelsLead = []
    dataLead = []
    context = {}

    querysetCustomer = Customer.objects.values('date_added__month').annotate(Count('status')).order_by('date_added__month').filter(status='Customer')[:4]
    
    querysetLead = Customer.objects.values('date_added__month').annotate(Count('status')).order_by('date_added__month').filter(status='Lead')[:4]
    

    for i, _ in enumerate(querysetCustomer):
        x, y = list(querysetCustomer[i].values())
        if x is None:
            continue
        labelsCustomer.append(calendar.month_name[x])
        dataCustomer.append(y)
    
    for i, _ in enumerate(querysetLead):
        x, y = list(querysetLead[i].values())
        if x is None:
            continue
        labelsLead.append(calendar.month_name[x])
        dataLead.append(y)

    context = {
        'labelsCustomer': labelsCustomer,
        'dataCustomer': dataCustomer,
        'labelsLead': labelsLead,
        'dataLead': dataLead
    }
    
    return context


def user_profile_picture(user):
    context = {}
    user = Agent.objects.values('profile_picture').filter(agent = user)
    for i, _ in enumerate(user):
        x = list(user[i].values())
        if x:
            url = "http://127.0.0.1:8000/media/" + x[0]
    context = {
        'url':url
    }
    return context