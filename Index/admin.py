from django.contrib import admin
from .models import ContactDetails, Testimonials, Video, Services, Gallery
admin.site.register(Video)
admin.site.register(Services)
admin.site.register(Gallery)
admin.site.register(ContactDetails)
admin.site.register(Testimonials)
#admin.site.register(Gallery)