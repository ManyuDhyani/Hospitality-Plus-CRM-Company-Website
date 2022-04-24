from django.shortcuts import render
from .models import Gallery, Testimonials, Video, Services
from Activities.models import Activities

#Index page function
def index(request):
    videos=Video.objects.first()
    activities = Activities.objects.filter(recommended=True)[:6]
    services=Services.objects.first()
    gallery=Gallery.objects.filter(recommended=True)[:10]
    testimonials=Testimonials.objects.filter(recommended=True)[:4]
    context={'videos':videos, 'activities':activities, 'services':services, 'gallery':gallery, 'testimonials':testimonials}
    print(videos.video1)
    return render(request, "index.html", context)