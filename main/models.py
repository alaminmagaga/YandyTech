from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date,timezone
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class HireCategory(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Scholarship(models.Model):
    image=models.ImageField(null=True, blank=True, default="chevening.png",upload_to="images/")
    title=models.CharField(max_length=1000, null=True , blank=True)
    slug=AutoSlugField(populate_from='title',null=True, default=None, unique=True)
    description=models.TextField(null=True , blank=True)
    website=models.CharField(max_length=1000, null=True, blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def snippet(self):
        return self.description[:50]+"..."

    def snippet1(self):
        return self.website[:27]+"..."
    def get_absolute_url(self):
        return reverse('home')

class Fellowship(models.Model):
    image=models.ImageField(null=True, blank=True,default="chevening.png", upload_to="images/")
    title=models.CharField(max_length=1000, null=True , blank=True)
    slug=AutoSlugField(populate_from='title',null=True, default=None, unique=True)
    description=models.TextField(null=True , blank=True)
    website=models.CharField(max_length=2000, null=True, blank=True)
    deadline=models.CharField(max_length=2000,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

   

    

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def snippet(self):
        return self.description[:50]+"..."

    def snippet1(self):
        return self.website[:27]+"..."

    def get_absolute_url(self):
        return reverse('home')


class Event(models.Model):
    image=models.ImageField(null=True, blank=True, default="images/chevening.png", upload_to="images/")
    title=models.CharField(max_length=1000, null=True , blank=True)
    description=models.TextField( null=True , blank=True)
    slug=AutoSlugField(populate_from='title',null=True, default=None, unique=True)
    website=models.CharField(max_length=2000, null=True, blank=True)
    eventdate=models.CharField(max_length=1000,null=True, blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
            
    def snippet(self):
        return self.description[:50]+"..."

    def snippet1(self):
        return self.website[:27]+"..."
    def get_absolute_url(self):
        return reverse('home')


class Track(models.Model):
    image=models.ImageField(null=True, blank=True, default="chevening.png", upload_to="images/")
    title=models.CharField(max_length=1000, null=True , blank=True)
    description=models.TextField( null=True , blank=True)
    slug=AutoSlugField(populate_from='title',null=True, default=None, unique=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    link=models.CharField(max_length=1000, null=False , blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def snippet(self):
        return self.description[:50]+"..."

    def get_absolute_url(self):
        return reverse('home')

   


class Community(models.Model):
    image=models.ImageField(null=True, blank=True,default="chevening.png", upload_to="images/")
    title=models.CharField(max_length=1000, null=True , blank=True)
    description=models.TextField(null=True , blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    def get_absolute_url(self):
        return reverse('home')

class Job(models.Model):
    image=models.ImageField(null=True, blank=True,default="chevening.png", upload_to="images/")
    position=models.CharField(max_length=1000, null=True , blank=True)
    company=models.CharField(max_length=2000, null=True , blank=True)
    location=models.CharField(max_length=1000, null=True , blank=True)
    amount=models.CharField(max_length=255, null=True , blank=True)
    category=models.CharField(max_length=255, null=True , blank=True)
    number=models.CharField(max_length=255, null=True , blank=True)
    women=models.CharField(max_length=255, null=True , blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    description=RichTextField( null=True , blank=True)
    link=models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.company




    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
   

    def get_absolute_url(self):
        #return reverse('article-detail',args=(str(self.id)))
        return reverse('home')

class Blog(models.Model):
    header_image=models.ImageField(default="chevening.png", upload_to="images/")
    title=models.CharField(max_length=1000)
    sub_title=models.CharField(max_length=1000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField()
    date=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=255, default='questions')


    def __str__(self):
        return self.title
    
    @property
    def image_url(self):
        if self.header_image and hasattr(self.header_image, 'url'):
            return self.header_image.url

    def get_absolute_url(self):
        return  reverse('home')

class Hire(models.Model):
    name=models.CharField(max_length=255, null=True , blank=True)
    skills=models.CharField(max_length=255, null=True , blank=True)
    location=models.CharField(max_length=255, null=True , blank=True)
    description=models.TextField(null=True , blank=True)
    cv=models.FileField(null=True, blank=True,upload_to="cv/")
    category=models.CharField(max_length=255, null=True , blank=True)
    twitter=models.CharField(max_length=255, null=True , blank=True)
    facebook=models.CharField(max_length=255, null=True , blank=True)
    linkedin=models.CharField(max_length=255, null=True , blank=True)
    website=models.CharField(max_length=255, null=True , blank=True)
    instagram=models.CharField(max_length=255, null=True , blank=True)
    email=models.CharField(max_length=255, null=True , blank=True)
    date=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name

    @property
    def cv_url(self):
        if self.cv and hasattr(self.cv, 'url'):
            return self.cv.url

  

    
    def get_absolute_url(self):
        return reverse('home')
    

class Article(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    new_slug=AutoSlugField(populate_from='title',null=True, default=None, unique=True)
    body=RichTextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',blank=True)
    author=models.CharField(max_length=1000, default='YandyTech')

    def get_absolute_url(self):
        return reverse('home')



    
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."









