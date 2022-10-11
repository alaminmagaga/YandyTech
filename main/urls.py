from django.urls import path
from .views import AddPostView
from . import views


urlpatterns = [
    path("",views.home,name="home"),
 
    # path("blog/",views.blog,name="blog"),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("support/",views.support,name="support"),
    path("community",views.community,name="community"),
    path("events/",views.events,name="events"),
    path("fellowship/",views.fellowship,name="fellowship"),
    path("hire/",views.hire,name="hire"),
    path("job/",views.job,name="job"),
    path("scholarship/",views.scholarship,name="scholarship"),
    path("about/",views.about,name="about"),
    # path("details/<str:cats>/",views.blogdetail,name="detail"),
    path("track/",views.track,name="track"),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category',views.CategoryL,name='category'),
    path('hire_category/<str:cats>/',views.HireCategoryView,name='hirecategory'),
    path('hirecategory',views.HireCategoryL,name='hirecategory'),
    path('add_post/',AddPostView.as_view(),name='add-post'),
    path('blog/',views.blog,name='blog'),
    path('details/<slug:slug>',views.blogdetail,name='details'),
   



]