from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .forms import LeadForm


def landing(request):
    return render(request, "landing.html")

class landingLeadFormView(generic.CreateView):
    template_name = 'landing.html'
    form_class = LeadForm
    # success_url = '/thanks/'

    # def form_valid(self, form):
    #     #form.send_email()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse("CRM:Landing-Lead-Page")

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