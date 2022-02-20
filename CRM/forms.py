from email.policy import default
from django import forms
from .models import Customer

class LeadForm(forms.ModelForm): 
    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass
    status = forms.CharField(widget = forms.HiddenInput(), required = False, initial="Lead")
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'events', 'phone_number', 'status']
        exclude = ('middle_name', 'age', 'number_of_calls', 'category_attended', 'email', 'converted_date', \
            'description', 'profile_picture', 'customer_details', 'agent', 'changed_by', 'history')