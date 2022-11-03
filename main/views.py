from multiprocessing import context
from django.shortcuts import render

from .models import Blog, Category, Community, Fellowship, Hire, HireCategory, Job, Scholarship,Event,Track,Article
from .forms import PostForm
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
# Create your views here.

class UserRegisterView(CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')



def home(request):
    return render(request,'index.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def support(request):
    return render(request,'support.html')






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
    
    template_name="add_job.html"
    fields='__all__'

class AddScholarshipPost(CreateView):
    model=Scholarship
    
    template_name="add_scholarship.html"
    fields='__all__'

class AddFellowshipPost(CreateView):
    model=Fellowship
    
    template_name="add_fellowship.html"
    fields='__all__'

class AddEventPost(CreateView):
    model=Event
    
    template_name="add_event.html"
    fields='__all__'

class AddCommunityPost(CreateView):
    model=Community
    
    template_name="add_community.html"
    fields='__all__'

class AddTrackPost(CreateView):
    model=Track
    
    template_name="add_track.html"
    fields='__all__'

class AddHirePost(CreateView):
    model=Hire
    
    template_name="add_hire.html"
    fields='__all__'

class UpdatePostView(UpdateView):
    model=Article
    template_name="update_post.html"
    fields=['title','slug','body']

class DeletePostView(DeleteView):
    model=Article
    template_name="delete_post.html"
    success_url=reverse_lazy('blog')


class EditJobView(UpdateView):
    model=Job
    template_name="edit_job.html"
    fields='__all__'
    success_url=reverse_lazy('job')

class DeleteJobView(DeleteView):
    model=Job
    template_name="delete_job.html"
    success_url=reverse_lazy('job')

class EditScholarshipView(UpdateView):
    model=Scholarship
    template_name="edit_scholarship.html"
    fields='__all__'
    success_url=reverse_lazy('scholarship')

class DeleteScholarshipView(DeleteView):
    model=Scholarship
    template_name="delete_scholarship.html"
    success_url=reverse_lazy('scholarship')


class EditFellowshipView(UpdateView):
    model=Fellowship
    template_name="edit_fellowship.html"
    fields='__all__'
    success_url=reverse_lazy('fellowship')

class DeleteFellowshipView(DeleteView):
    model=Fellowship
    template_name="delete_fellowship.html"
    success_url=reverse_lazy('fellowship')
    

class EditEventView(UpdateView):
    model=Event
    template_name="edit_event.html"
    fields='__all__'
    success_url=reverse_lazy('events')

class DeleteEventView(DeleteView):
    model=Event
    template_name="delete_event.html"
    success_url=reverse_lazy('events')

class EditTrackView(UpdateView):
    model=Track
    template_name="edit_track.html"
    fields='__all__'
    success_url=reverse_lazy('track')

class DeleteTrackView(DeleteView):
    model=Track
    template_name="delete_track.html"
    success_url=reverse_lazy('track')

class EditHireView(UpdateView):
    model=Hire
    template_name="edit_hire.html"
    fields='__all__'
    success_url=reverse_lazy('hire')

class DeleteHireView(DeleteView):
    model=Hire
    template_name="delete_hire.html"
    success_url=reverse_lazy('hire')


def community(request):
    communitys=Community.objects.all().order_by('date')
    context={'communitys':communitys}
    return render(request,'community.html',context)

def events(request):
    events=Event.objects.all().order_by('date')
    context={'events':events}
    return render(request,'events.html',context)

def fellowship(request):
    fellowships=Fellowship.objects.all().order_by('date')
    context={'fellowships':fellowships}
    return render(request,'fellowship.html',context)

def hire(request):
    hires=Hire.objects.all().order_by('date')
    cate=HireCategory.objects.all()
    context={'hires':hires,'cate':cate}
    return render(request,'hire.html',context)



def scholarship(request):
    scholarships=Scholarship.objects.all().order_by('date')
    context={'scholarships':scholarships}
    return render(request,'scholarship.html',context)

def about(request):
    return render(request,'about.html')

def track(request):
    tracks=Track.objects.all().order_by('date')
    context={'tracks':tracks}
    return render(request,'track.html',context)

def CategoryView(request,cats):
    category_post=Job.objects.filter(category=cats)
    cate=Category.objects.all()
    context={'cats':cats ,'category_post':category_post,'cate':cate}
    return render(request,'category.html',context)

def CategoryL(request):
    catelist=Category.objects.all()
    context={'catelist':catelist}
    return render(request,'buy.html',context)


def HireCategoryView(request,cats):
    category_post=Hire.objects.filter(category=cats)
    cate=HireCategory.objects.all()
    context={'cats':cats ,'category_post':category_post,'cate':cate}
    return render(request,'hire_category.html',context)

def HireCategoryL(request):
    cate=HireCategory.objects.all()
    context={'cate':cate}
    return render(request,'hire.html',context)

