from django.contrib import admin
from .models import Blog, HireCategory, Hire, HireCategory, Job, Scholarship,Fellowship,Event,Track,Community,Category

# Register your models here.
admin.site.register(Scholarship)
admin.site.register(Fellowship)
admin.site.register(Event)
admin.site.register(Track)
admin.site.register(Community)
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Hire)
admin.site.register(HireCategory)