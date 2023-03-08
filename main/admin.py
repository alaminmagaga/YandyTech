from django.contrib import admin
from .models import  HireCategory, Hire, HireCategory, Job, Scholarship,Fellowship,Event,Track,Community,Category,Article,BlogCategory,Comment

# Register your models here.
admin.site.register(Scholarship)
admin.site.register(Fellowship)
admin.site.register(Event)
admin.site.register(Track)
admin.site.register(Community)
admin.site.register(Job)
admin.site.register(Category)

admin.site.register(Hire)
admin.site.register(HireCategory)
admin.site.register(Article)
admin.site.register(BlogCategory)
admin.site.register(Comment)