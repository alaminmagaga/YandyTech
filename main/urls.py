from django.urls import path
from .views import AddPostView, JobView,JobDetailView
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("support/",views.support,name="support"),
    path("community",views.community,name="community"),
    path("events/",views.events,name="events"),
    path("fellowship/",views.fellowship,name="fellowship"),
    path("hire/",views.hire,name="hire"),
    path("scholarship/",views.scholarship,name="scholarship"),
    path("about/",views.about,name="about"),
    path("track/",views.track,name="track"),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category',views.CategoryL,name='buy'),
    path('hire_category/<str:cats>/',views.HireCategoryView,name='hirecategory'),
    path('hirecategory',views.HireCategoryL,name='hirecategory'),
    path('add_post/',AddPostView.as_view(),name='add-post'),
    path('blog/',views.blog,name='blog'),
    path('details/<slug:slug>',views.blogdetail,name='details'),
    path("job/",JobView.as_view(),name="job"),
    path('job/<int:pk>', JobDetailView.as_view() , name='jobdetail'),
   



]