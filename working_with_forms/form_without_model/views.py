from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactUsForm

# Create your views here.
def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            
            print('name:', form.cleaned_data['name'])
            print('email:', form.cleaned_data['email'])
            print('message:', form.cleaned_data['message'])
            
            # do what ever you want to do
            # for example, send email 

            return HttpResponseRedirect('/')
    else:
        form = ContactUsForm()
    
    return render(request, "contactus.html", {'form':form})
