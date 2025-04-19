from django.shortcuts import render , redirect ,  get_object_or_404
from app.forms import *
from django.core.mail import EmailMultiAlternatives , EmailMessage
from django.conf import settings 
from .models import *
from django.db.models import Q

def index(request):
    return render(request , 'index.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
           # category = form.cleaned_data['category']
           # subject = f"Contact - {category} from {name}"
            subject = f"Contact - DevByCosmin from {name}"
            EmailMessage(
               subject,
               message,
               email, 
               [settings.EMAIL_HOST_USER], 
               [],
               reply_to=[email] 
           ).send()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def support_developer(request):
    return render(request , 'support.html')


def BlogPosts(request):
    search_post = request.GET.get('search')

    if search_post:
      posts = BlogPost.objects.filter(Q(title__icontains=search_post))
    else:
      posts = BlogPost.objects.all()

    return render(request , 'blog/blog.html' , {'posts':posts , 'search_query': search_post})
