from django.urls import path
from .views import landing, landingLeadFormView

app_name = 'CRM'

urlpatterns = [
    path('book-your-spot/', landing, name="Landing-Lead-Page"),
    path('', landingLeadFormView.as_view()),
    ]