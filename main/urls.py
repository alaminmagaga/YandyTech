from django.urls import path
from .views import AddBlogPost, JobView,JobDetailView,AddJobPost,AddCommunityPost,AddTrackPost,AddScholarshipPost,AddFellowshipPost,AddHirePost,AddEventPost,UpdatePostView,DeletePostView,EditJobView,DeleteJobView,EditScholarshipView,DeleteScholarshipView,EditFellowshipView,EditEventView,EditTrackView,EditHireView,DeleteFellowshipView,DeleteEventView,DeleteTrackView,DeleteHireView,UserRegisterView
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('profile/',views.profile,name='profile'),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("support/",views.support,name="support"),
    path("community",views.community,name="community"),
    path("events/",views.events,name="events"),
    path('events/edit/<int:pk>',EditEventView.as_view(),name='edit-event'),
    path('events/<int:pk>/remove',DeleteEventView.as_view(),name='delete-event'),
    path("fellowship/",views.fellowship,name="fellowship"),
    path('fellowship/edit/<int:pk>',EditFellowshipView.as_view(),name='edit-fellowship'),
    path('fellowship/<int:pk>/remove',DeleteFellowshipView.as_view(),name='delete-fellowship'),
    path("hire/",views.hire,name="hire"),
    path('hire/edit/<int:pk>',EditHireView.as_view(),name='edit-hire'),
    path('hire/<int:pk>/remove',DeleteHireView.as_view(),name='delete-hire'),
    path("scholarship/",views.scholarship,name="scholarship"),
    path('scholarship/edit/<int:pk>',EditScholarshipView.as_view(),name='edit-scholarship'),
    path('scholarship/<int:pk>/remove',DeleteScholarshipView.as_view(),name='delete-scholarship'),
    path("about/",views.about,name="about"),
    path("digilab/",views.track,name="track"),
    path('digilab/edit/<int:pk>',EditTrackView.as_view(),name='edit-track'),
    path('digilab/<int:pk>/remove',DeleteTrackView.as_view(),name='delete-track'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category',views.CategoryL,name='buy'),
    path('hire_category/<str:cats>/',views.HireCategoryView,name='hirecategory'),
    path('hirecategory',views.HireCategoryL,name='hirecategory'),
    path('add_post/',AddBlogPost.as_view(),name='add-post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete-post'),
    
    path('blog/',views.blog,name='blog'),
    path('details/<slug:slug>',views.blogdetail,name='details'),
    path("job/",JobView.as_view(),name="job"),
    path('job/<int:pk>', JobDetailView.as_view() , name='jobdetail'),
    path('job/edit/<int:pk>',EditJobView.as_view(),name='edit-job'),
    path('job/<int:pk>/remove',DeleteJobView.as_view(),name='delete-job'),
    path('add_job/',AddJobPost.as_view(),name='add-job'),
    
    path('add_scholarship/',AddScholarshipPost.as_view(),name='add-scholarship'),
    path('add_fellowship/',AddFellowshipPost.as_view(),name='add-fellowship'),
    path('add_digilab/',AddTrackPost.as_view(),name='add-track'),
    path('add_event/',AddEventPost.as_view(),name='add-event'),
    path('add_community/',AddCommunityPost.as_view(),name='add-community'),
    path('add_hire/',AddHirePost.as_view(),name='add-hire'),
   



]