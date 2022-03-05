from django import forms
from django.core.exceptions import ValidationError # import this
from django.forms.fields import EmailField
from django.forms.widgets import Textarea

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # add this
    def clean_email(self):
        """
        clean the email field to prevent users from using example@example.com
        """
        email_address = self.cleaned_data['email'] # email is stored in cleaned_data by clean() method called by is_valid()

        if email_address == 'example@example.com':
            raise ValidationError("this email cannot be used, please enter another email address")
        
        return email_address
