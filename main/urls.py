from django.urls import path
from .views import AddPostView
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("blog/",views.blog,name="blog"),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("community",views.community,name="community"),
    path("events/",views.events,name="events"),
    path("fellowship/",views.fellowship,name="fellowship"),
    path("hire/",views.hire,name="hire"),
    path("job/",views.job,name="job"),
    path("scholarship/",views.scholarship,name="scholarship"),
    path("about/",views.about,name="about"),
    path("details/",views.blogdetail,name="blog-detail"),
    path("track/",views.track,name="track"),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category',views.CategoryL,name='category'),

    path('hire_category/<str:cats>/',views.HireCategoryView,name='hirecategory'),
    path('hirecategory',views.HireCategoryL,name='hirecategory'),

    path('add_post/',AddPostView.as_view(),name='add-post'),



]