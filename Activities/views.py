from django.shortcuts import render, get_object_or_404

from Index.models import ContactDetails
from .models import Activities

def activityDetail(request, slug):
    activity = get_object_or_404(Activities, slug=slug)
    contact = ContactDetails.objects.first()
    context={'activity':activity, 'contact':contact}
    return render(request, "activityDetail.html", context)