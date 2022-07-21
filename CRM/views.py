from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.db.models import Count, Q
from django.contrib.admin.views.decorators import staff_member_required

from CRM.models import Customer
from .forms import LeadForm
from Activities.models import Activities
from Index.models import ContactDetails

class landingLeadFormView(generic.CreateView):
    template_name = 'landing.html'
    form_class = LeadForm
    # success_url = '/thanks/'

    # def form_valid(self, form):
    #     #form.send_email()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse("CRM:Success")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.save()
        # send_mail(
        #     subject="A lead has been created",
        #     message="Go to the site to see the new lead",
        #     from_email="test@test.com",
        #     recipient_list=["test2@test.com"]
        # )
        # messages.success(self.request, "You have successfully created a lead")
        return super(landingLeadFormView, self).form_valid(form)



def thankyou(request):
    return render(request, "thankYou.html")


#Graph Analysis for CRM data
@staff_member_required
def pie_chart_category(request):
    labels = []
    data = []

    queryset = Customer.objects.values('category_attended__title').annotate(trend_count=Count('category_attended__title')).order_by('-trend_count')
    
    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)
        
    return render(request, 'CRM/pieChart.html', {
        'labels': labels,
        'data': data,
    })

@staff_member_required
def pie_chart_gender(request):
    labels = []
    data = []

    queryset = Customer.objects.values('gender').annotate(gender_ratio=Count('gender')).order_by('gender_ratio')

    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)

    return render(request, 'CRM/pieChart.html', {
        'labels': labels,
        'data': data,
    })

@staff_member_required
def bar_chart_lead_customer_ratio(request):
    labels = []
    data = []

    queryset = Customer.objects.values('status').annotate(lead_customer_ratio=Count('status')).order_by('lead_customer_ratio')

    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        if x is None:
            continue
        labels.append(x)
        data.append(y)

    return render(request, 'CRM/barChart.html', {
        'labels': labels,
        'data': data,
    })


def search(request):
    contact = ContactDetails.objects.first()
    query = request.GET.get('search')
    print(query)
    activities = Activities.objects.all()
    search_result = activities.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    print(search_result)
    context = {
        'activities': search_result,
        'contact': contact
    }
    return render(request, 'search.html', context)