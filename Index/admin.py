from django.contrib import admin
from .models import AboutUs, ContactDetails, Newsletter, PrivacyPolicy, Quotes, TermsCondition, Testimonials, Video, Services, Gallery, Blogs
admin.site.register(Video)
admin.site.register(Services)
admin.site.register(Gallery)
admin.site.register(ContactDetails)
admin.site.register(Testimonials)
admin.site.register(Quotes)
admin.site.register(Blogs)
admin.site.register(AboutUs)
admin.site.register(Newsletter)
admin.site.register(TermsCondition)
admin.site.register(PrivacyPolicy)