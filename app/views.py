from django.shortcuts import render , redirect ,  get_object_or_404
from app.forms import *
from django.core.mail import EmailMultiAlternatives 
from django.conf import settings 
from .models import *
from django.db.models import Q
from django.contrib import messages

def index(request):

    posts = BlogPost.objects.all()
    projects = ProjectPost.objects.all()
    return render(request , 'index.html' ,  {'posts':posts  , 'projects':projects})

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
            EmailMultiAlternatives(
               subject,
               message,
               email, 
               [settings.EMAIL_HOST_USER], 
               [],
               reply_to=[email] 
           ).send()
            return redirect('contact')
        else:
            messages.error(request, "Form or CAPTCHA is invalid. Please check your input.")
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

def blog_detail(request , post_id):
    post = get_object_or_404(BlogPost , id=post_id)
    return render(request , 'blog/blog_detail.html' , {'post':post})

def services_page(request):
    return render(request , 'services.html')