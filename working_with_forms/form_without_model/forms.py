from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
