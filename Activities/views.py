from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from Index.models import ContactDetails
from .models import Activities

def activityDetail(request, slug):
    recommendations = Activities.objects.order_by('?')[:4]

    activity = get_object_or_404(Activities, slug=slug)
    contact = ContactDetails.objects.first()
    context={'activity':activity, 'contact': contact, "recommendations": recommendations}
    return render(request, "activityDetail.html", context)

class activitiesView(ListView):
    model = Activities
    paginate_by = 6
    context_object_name = 'activities'
    template_name = 'activities.html'

