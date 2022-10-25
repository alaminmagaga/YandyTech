from multiprocessing import context
from django.shortcuts import render

from .models import Blog, Category, Community, Fellowship, Hire, HireCategory, Job, Scholarship,Event,Track,Article
from .forms import PostForm
from django.views.generic import CreateView,DetailView,ListView
# Create your views here.

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
    return render(request,'article.html',context)

def blogdetail(request,slug):
    article=Article.objects.get(slug=slug)
    context={'article':article}
    return render(request,'article_details.html',context)



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
   




class AddPostView(CreateView):
    model=Blog
    form_class=PostForm
    template_name="add_post.html"
    #fields='__all__'
    
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

