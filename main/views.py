from multiprocessing import context
from django.shortcuts import render
from .models import Blog, Category, Community, Fellowship, Hire, HireCategory, Job, Scholarship,Event,Track,Article
from .forms import *
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm



# User Registration
class UserRegisterView(CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

def profile(request):
    return render(request,'profile.html')
# End Registration

# home Section
def home(request):
    return render(request,'index.html')

# Terms Section
def terms(request):
    return render(request,'terms.html')

# Privacy Section
def privacy(request):
    return render(request,'privacy.html')
    
# Support Section
def support(request):
    return render(request,'support.html')

# About Section
def about(request):
    return render(request,'about.html')






#job section
class JobView(ListView):
    model=Job
    template_name='job.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(JobView, self).get_context_data(*args,**kwargs)
        context['cat_menu']= cat_menu
        return context

class JobDetailView(DetailView):
    model=Job
    template_name='job_detail.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(JobDetailView, self).get_context_data(*args,**kwargs)
        context['cat_menu']= cat_menu
        return context

class AddJobPost(CreateView):
    model=Job
    form_class=JobForm
    template_name="add_job.html"
    success_url=reverse_lazy('job')

class EditJobView(UpdateView):
    model=Job
    form_class=EditJob
    template_name="edit_job.html"
    success_url=reverse_lazy('job')

class DeleteJobView(DeleteView):
    model=Job
    template_name="delete_job.html"
    success_url=reverse_lazy('job')
# End Job


# Scholarship Section

def scholarship(request):
    scholarships=Scholarship.objects.all().order_by('date')
    context={'scholarships':scholarships}
    return render(request,'scholarship.html',context)

class AddScholarshipPost(CreateView):
    model=Scholarship
    form_class = ScholarshipForm
    template_name="add_scholarship.html"
    success_url=reverse_lazy('scholarship')



class EditScholarshipView(UpdateView):
    model=Scholarship
    form_class=EditScholarship
    template_name="edit_scholarship.html"
    success_url=reverse_lazy('scholarship')

class DeleteScholarshipView(DeleteView):
    model=Scholarship
    template_name="delete_scholarship.html"
    success_url=reverse_lazy('scholarship')

# End Scholarship


# Fellowship Section
def fellowship(request):
    fellowships=Fellowship.objects.all().order_by('date')
    context={'fellowships':fellowships}
    return render(request,'fellowship.html',context)

class AddFellowshipPost(CreateView):
    model=Fellowship
    form_class = FellowshipForm
    template_name="add_fellowship.html"
    success_url=reverse_lazy('fellowship')


class EditFellowshipView(UpdateView):
    model=Fellowship
    form_class=EditFellowship
    template_name="edit_fellowship.html"
    
    success_url=reverse_lazy('fellowship')

class DeleteFellowshipView(DeleteView):
    model=Fellowship
    template_name="delete_fellowship.html"
    success_url=reverse_lazy('fellowship')
# End Fellowship



# Event Section

def events(request):
    events=Event.objects.all().order_by('date')
    context={'events':events}
    return render(request,'events.html',context)
    
class AddEventPost(CreateView):
    model=Event
    form_class=EventForm
    template_name="add_event.html"
    success_url=reverse_lazy('events')

class EditEventView(UpdateView):
    model=Event
    form_class=EditEvent
    template_name="edit_event.html"
    success_url=reverse_lazy('events')

class DeleteEventView(DeleteView):
    model=Event
    template_name="delete_event.html"
    success_url=reverse_lazy('events')


# End Event


# Community Section
def community(request):
    communitys=Community.objects.all().order_by('date')
    context={'communitys':communitys}
    return render(request,'community.html',context)

class AddCommunityPost(CreateView):
    model=Community
    template_name="add_community.html"
    fields='__all__'
# End Community

# Track Section
def track(request):
    tracks=Track.objects.all().order_by('date')
    context={'tracks':tracks}
    return render(request,'track.html',context)

class AddTrackPost(CreateView):
    model=Track
    form_class=TrackForm
    template_name="add_track.html"

class EditTrackView(UpdateView):
    model=Track
    form_class=EditTrack
    template_name="edit_track.html"
    success_url=reverse_lazy('track')

class DeleteTrackView(DeleteView):
    model=Track
    template_name="delete_track.html"
    success_url=reverse_lazy('track')

# End Track


# Blog Section

def blog(request):
    articles=Article.objects.all().order_by('date')
    context={'articles':articles}
    print(articles)
    return render(request,'blog.html',context)

def blogdetail(request,slug):
    article=Article.objects.get(slug=slug)
    context={'article':article}
    return render(request,'blog_details.html',context)

class AddBlogPost(CreateView):
    model=Article
    form_class=PostForm
    template_name="add_post.html"
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Article
    form_class = EditForm
    template_name="update_post.html"
    #fields=['title','slug','body']

class DeletePostView(DeleteView):
    model=Article
    template_name="delete_post.html"
    success_url=reverse_lazy('blog')
# End Blog


# Hire Section
def hire(request):
    hires=Hire.objects.all().order_by('date')
    cate=HireCategory.objects.all()
    context={'hires':hires,'cate':cate}
    return render(request,'hire.html',context)


class AddHirePost(CreateView):
    model=Hire
    form_class=HireForm
    template_name="add_hire.html"
    success_url=reverse_lazy('hire')

class EditHireView(UpdateView):
    model=Hire
    form_class=EditHire
    template_name="edit_hire.html"
    success_url=reverse_lazy('hire')

class DeleteHireView(DeleteView):
    model=Hire
    template_name="delete_hire.html"
    success_url=reverse_lazy('hire')

def HireCategoryView(request,cats):
    category_post=Hire.objects.filter(category=cats)
    cate=HireCategory.objects.all()
    context={'cats':cats ,'category_post':category_post,'cate':cate}
    return render(request,'hire_category.html',context)

def HireCategoryL(request):
    cate=HireCategory.objects.all()
    context={'cate':cate}
    return render(request,'hire.html',context)

# End hire


# Category
def CategoryView(request,cats):
    category_post=Job.objects.filter(category=cats)
    cate=Category.objects.all()
    context={'cats':cats ,'category_post':category_post,'cate':cate}
    return render(request,'category.html',context)

def CategoryL(request):
    catelist=Category.objects.all()
    context={'catelist':catelist}
    return render(request,'buy.html',context)

# End Category


