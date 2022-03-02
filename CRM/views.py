from re import template
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.db.models import Count

from CRM.models import Customer
from .forms import LeadForm


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

def pie_chart(request):
    labels = []
    data = []

    queryset = Customer.objects.values('category_attended__title').annotate(trend_count=Count('category_attended__title')).order_by('-trend_count')
<<<<<<< HEAD
    # print(queryset[1])
    
    for i, cat in enumerate(queryset):
        x, y = list(queryset[i].values())
        labels.append(x)
        data.append(y)

=======
    for i, cat in enumerate(queryset):
        for j, keys in enumerate(queryset[i]):
            print(queryset)
            print(queryset[j][keys])
            # x, y = queryset[j][keys], queryset[j]
            # print("x:", x, "y:", y)
            # x, y = queryset[j].split()
            # labels.append(str(queryset[j][keys]))
            # data.append(str(queryset[j][keys]))
        
>>>>>>> 6f26851e12cc98c9741392944763a16e7ac950ef

    return render(request, 'CRM/pieChart.html', {
        'labels': labels,
        'data': data,
    })
