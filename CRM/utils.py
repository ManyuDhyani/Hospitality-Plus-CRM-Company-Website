from .models import Customer
from django.db.models import Count

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
        'datalLeadCustomer': data,
    }

    return context
