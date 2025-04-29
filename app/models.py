from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField('image' , null=False , blank=False) 
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

class ProjectPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField('image' , null=False , blank=False) 
