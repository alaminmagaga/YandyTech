from multiprocessing import context
from django.shortcuts import render
from .models import Category, Community, Fellowship, Hire, HireCategory, Job, Scholarship,Event,Track,Article,BlogCategory
from .forms import *
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import HttpResponse
from django.urls import path
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage

import os







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



class JobView(ListView):
    model=Job
    template_name='job.html'
    paginate_by = 10 # number of items per page
    ordering=['-id']
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


from django.core.paginator import Paginator

def scholarship(request):
    scholarships=Scholarship.objects.all().order_by('date')
    paginator = Paginator(scholarships, 4)  # Show 10 scholarships per page
    page = request.GET.get('page')
    scholarships = paginator.get_page(page)
    context={'scholarships':scholarships}
    return render(request,'scholarship.html',context)



def scholarshipdetail(request,slug):
    scholarship=Scholarship.objects.get(slug=slug)
    context={'scholarship':scholarship}
    return render(request,'scholarship_details.html',context)

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
    paginator = Paginator(fellowships, 4)  # Show 10  per page
    page = request.GET.get('page')
    fellowships = paginator.get_page(page)
    context={'fellowships':fellowships}
    return render(request,'fellowship.html',context)



def fellowshipdetail(request,slug):
    fellowship=Fellowship.objects.get(slug=slug)
    context={'fellowship':fellowship}
    return render(request,'fellowship_details.html',context)


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
    paginator = Paginator(events, 4)  # Show 10  per page
    page = request.GET.get('page')
    events = paginator.get_page(page)
    context={'events':events}
    return render(request,'events.html',context)




def eventdetail(request,slug):
    event=Event.objects.get(slug=slug)
    context={'event':event}
    return render(request,'event_details.html',context)
    
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
    paginator = Paginator(tracks, 6)  # Show 10  per page
    page = request.GET.get('page')
    tracks = paginator.get_page(page)
    context={'tracks':tracks}
    ordering=['-id']
    return render(request,'track.html',context)




def trackdetail(request,slug):
    track=Track.objects.get(slug=slug)
    context={'track':track}
    return render(request,'track_details.html',context)

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
    larticles = Article.objects.all().order_by('date')[1:4]
    articles = Article.objects.all().order_by('date')[2:4]
    latest_article = Article.objects.latest('date')
    view_article = Article.objects.all().order_by('-views')[:5]
    category = get_object_or_404(BlogCategory, name='Enterprenuership')
    category_articles = Article.objects.filter(category=category).order_by('date')[:2]
    latest_articles = Article.objects.filter(category=category).order_by('-date')[:1]
    category_views = Article.objects.filter(category=category).order_by('-views').first()
    top_category_view = Article.objects.filter(category=category).order_by('-views')[:8]

    tech_category = get_object_or_404(BlogCategory, name='Tech')
    tech_articles = Article.objects.filter(category=tech_category).order_by('date')[:8]
    latest_tech = Article.objects.filter(category=tech_category).order_by('-date')[:1]
    top_tech_view = Article.objects.filter(category=tech_category).order_by('-views')[:2]
    second_tech_view = Article.objects.filter(category=tech_category).order_by('-views')[1:2]
    cate=BlogCategory.objects.all()

    
   

    context = {'larticles': larticles, 'articles': articles, 'latest_article': latest_article, 'view_article': view_article,'cate':cate,'category_articles': category_articles,'latest_articles':latest_articles,'category_views':category_views,'top_category_view':top_category_view, 'tech_articles':tech_articles, 'latest_tech':latest_tech, 'top_tech_view':top_tech_view, 'second_tech_view':second_tech_view}
    return render(request, 'blog.html', context)


    
def blogdetail(request,slug):
    article=Article.objects.get(slug=slug)

    # Handle comment form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_id = form.cleaned_data.get('parent')
            if parent_id:
                parent = Comment.objects.get(id=parent_id)
                comment = form.save(commit=False)
                comment.article = article
                comment.parent = parent
                comment.save()
            else:
                comment = form.save(commit=False)
                comment.article = article
                comment.save()
            return redirect('details', slug=slug)
    else:
        form = CommentForm()

    # Increase the view count
    if request.method == 'GET':
        article.views += 1
        article.save()

    # Retrieve comments for the article
    comments = Comment.objects.filter(article=article)

    context={'article':article, 'form': form, 'comments': comments}
    return render(request,'blog_details.html',context)

def reply(request, slug, comment_id):
    article = get_object_or_404(Article, slug=slug)
    parent_comment = get_object_or_404(Comment, id=comment_id)
    
    # Handle reply comment form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.article = article
            reply.parent = parent_comment  # set the parent comment instance
            reply.save()
            return redirect('details', slug=slug)
    else:
        form = CommentForm()

    context = {'form': form, 'parent_comment': parent_comment}
    return render(request, 'reply.html', context)





def BlogCategoryView(request,cats):
    category_post=Article.objects.filter(category=cats)
    cate=BlogCategory.objects.all()
    context={'cats':cats ,'category_post':category_post,'cate':cate}
    ordering=['id']
    return render(request,'blog_category.html',context)

def BlogCategoryL(request):
    cate=BlogCategory.objects.all()
    context={'cate':cate}
    ordering=['-id']
    return render(request,'blog.html',context)

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
    hires=Hire.objects.all().order_by('-id')
    paginator = Paginator(hires, 9)  # Show 10  per page
    page = request.GET.get('page')
    hires = paginator.get_page(page)
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
    ordering=['id']
    return render(request,'hire_category.html',context)

def HireCategoryL(request):
    cate=HireCategory.objects.all()
    context={'cate':cate}
    ordering=['-id']
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


