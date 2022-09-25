from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

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
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=100, null=True , blank=True)
    description=models.TextField(max_length=255, null=True , blank=True)
    website=models.CharField(max_length=255, null=True, blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Fellowship(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=100, null=True , blank=True)
    description=models.TextField(max_length=255, null=True , blank=True)
    website=models.CharField(max_length=255, null=True, blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Event(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=100, null=True , blank=True)
    description=models.TextField(max_length=255, null=True , blank=True)
    website=models.CharField(max_length=255, null=True, blank=True)
    eventdate=models.CharField(max_length=255,null=True, blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Track(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=100, null=True , blank=True)
    description=models.TextField(max_length=255, null=True , blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Community(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=100, null=True , blank=True)
    description=models.TextField(max_length=255, null=True , blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Job(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    position=models.CharField(max_length=100, null=True , blank=True)
    company=models.CharField(max_length=255, null=True , blank=True)
    location=models.CharField(max_length=100, null=True , blank=True)
    amount=models.CharField(max_length=255, null=True , blank=True)
    category=models.CharField(max_length=255, null=True , blank=True)
    number=models.CharField(max_length=255, null=True , blank=True)
    women=models.CharField(max_length=255, null=True , blank=True)
    deadline=models.CharField(max_length=255,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Blog(models.Model):
    header_image=models.ImageField(null=True, blank=True, upload_to="images/")
    title=models.CharField(max_length=255)
    sub_title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(max_length=100, null=True , blank=True)
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
    description=models.TextField(max_length=255, null=True , blank=True)
    category=models.CharField(max_length=255, null=True , blank=True)
    twitter=models.CharField(max_length=255, null=True , blank=True)
    facebook=models.CharField(max_length=255, null=True , blank=True)
    linkedin=models.CharField(max_length=255, null=True , blank=True)
    website=models.CharField(max_length=255, null=True , blank=True)
    instagram=models.CharField(max_length=255, null=True , blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    









