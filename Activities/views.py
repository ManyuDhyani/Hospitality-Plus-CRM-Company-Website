from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from CRM.models import PageView
from Index.models import ContactDetails
from .models import Activities

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def activityDetail(request, slug):
    recommendations = Activities.objects.order_by('?')[:4]

    activity = get_object_or_404(Activities, slug=slug)

    ip = get_client_ip(request)
    if ip:
        PageView.objects.get_or_create(ip=ip, page=activity.title)

    contact = ContactDetails.objects.first()
    context={'activity':activity, 'contact': contact, "recommendations": recommendations}
    return render(request, "activityDetail.html", context)

class activitiesView(ListView):
    model = Activities
    paginate_by = 6
    context_object_name = 'activities'
    template_name = 'activities.html'

