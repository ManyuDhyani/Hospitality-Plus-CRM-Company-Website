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
    
    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({"class": "form-control"})
    #     self.fields['first_name'].widget.attrs.update({'class': 'border border-2 border-primary rounded'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'border border-2 border-primary rounded'})
        self.fields['gender'].widget.attrs.update({'class': 'border border-2 border-primary rounded'})
        self.fields['events'].widget.attrs.update({'class': 'border border-2 border-primary rounded'})
    #     self.fields['phone_number'].widget.attrs.update({'class': 'border border-2 border-primary rounded'})
    #     self.fields['phone_number'].widget.attrs.update({'placeholder': 'Search'})