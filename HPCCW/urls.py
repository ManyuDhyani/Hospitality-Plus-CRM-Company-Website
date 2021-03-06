from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views
from Index.views import index, galleryView, aboutus, privacyPolicy, termsCondition

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
    path('booking/', include('CRM.urls', namespace='CRM')),
    path('dashboard/', include('Dashboard.urls', namespace='Dashboard')),
    path('activities/', include('Activities.urls', namespace='Activities')),

    #Index app urls
    path('', index, name="index"),
    path('gallery/', galleryView.as_view(), name="gallery"),
    path('about-us/', aboutus, name="aboutus"),
    path('privacy-policy/', privacyPolicy, name="privacyPolicy"),
    path('terms-and-condition/', termsCondition, name="termsCondition"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Company Administration"
admin.site.index_title = "Company Administrator & Database"