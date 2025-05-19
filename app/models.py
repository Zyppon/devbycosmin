from django.db import models
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    image = CloudinaryField('image' , null=False , blank=False) 
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title

class ProjectPost(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image' , null=False , blank=False) 
    live_url = models.URLField()
    github_url = models.URLField()
    def __str__(self):

        return self.title
