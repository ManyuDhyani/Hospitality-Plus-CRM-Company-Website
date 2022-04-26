from django.shortcuts import render
from .models import ContactDetails, Gallery, Quotes, Testimonials, Video, Services, Blogs
from Activities.models import Activities
import requests

#Index page function
def index(request):
    videos=Video.objects.first()
    activities = Activities.objects.filter(recommended=True)[:6]
    services=Services.objects.first()
    gallery=Gallery.objects.filter(recommended=True)[:10]
    testimonials=Testimonials.objects.filter(recommended=True)[:4]
    quotes=Quotes.objects.first()
    contact = ContactDetails.objects.first()

    # For the Blogs from HashStrix
    response = requests.get('https://www.hashstrix.com/api/traveloftindia/')
    json_response = response.json()
    for i in json_response:
        Blogs.objects.get_or_create(
            title = i['title'],
            overview = i['overview'],
            thumbnail = i['thumbnail'],
            timestamp = i['timestamp'],
            author = i['author']['user']['username'], 
            blog_url = "https://www.hashstrix.com/post/" + i['slug'] + "/"
    )
    blogs = Blogs.objects.filter(recommended=True)[:3]
    
    context={
        'videos':videos, 
        'activities':activities, 
        'services':services, 
        'gallery':gallery, 
        'testimonials':testimonials, 
        'quotes':quotes, 
        'blogs': blogs,
        'contact':contact
        }

    return render(request, "index.html", context)