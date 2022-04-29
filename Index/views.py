from django.shortcuts import render
from django.views.generic.list import ListView
import requests

from .models import AboutUs, ContactDetails, Gallery, Quotes, Testimonials, Video, Services, Blogs
from Activities.models import Activities
from CRM.models import Newsletter

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

    # For Newsletter
    if request.method == "POST":
        email = request.POST["email"]
        new_newsletter_signup = Newsletter()
        new_newsletter_signup.email = email
        new_newsletter_signup.save()
    
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

class galleryView(ListView):
    model = Gallery 
    paginate_by = 6
    context_object_name = 'gallery'
    template_name = 'gallery.html'
    ordering = ['-modified']

# class aboutus(ListView):
#     queryset = AboutUs.objects.first()
#     template_name = 'aboutus.html'
#     context_object_name = 'aboutus'

def aboutus(request):
    aboutus = AboutUs.objects.first()
    return render(request, 'aboutus.html', {'aboutus': aboutus})