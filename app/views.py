from django.shortcuts import render , redirect
from forms import *
from django.core.mail import EmailMultiAlternatives , EmailMessage
from django.conf import settings 


def index(request):
    return render(request , 'index.html')

def contact(request):
    return render(request , 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            category = form.cleaned_data['category']
            subject = f"Contact - {category} from {name}"
            EmailMessage(
               subject,
               message,
               email, 
               [settings.EMAIL_HOST_USER], 
               [],
               reply_to=[email] 
           ).send()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})