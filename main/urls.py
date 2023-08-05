from django.urls import path
from .views import AddBlogPost, JobView,JobDetailView,AddJobPost,AddCommunityPost,AddTrackPost,AddScholarshipPost,AddFellowshipPost,AddHirePost,AddEventPost,UpdatePostView,DeletePostView,EditJobView,DeleteJobView,EditScholarshipView,DeleteScholarshipView,EditFellowshipView,EditEventView,EditTrackView,EditHireView,DeleteFellowshipView,DeleteEventView,DeleteTrackView,DeleteHireView,UserRegisterView
from . import views





urlpatterns = [
    path("",views.home,name="home"),
    path('joinus/',views.joinus,name="joinus"),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('accounts/profile/',views.profile,name='profile'),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("support/",views.support,name="support"),
    path("community",views.community,name="community"),
    path("events/",views.events,name="events"),
    path('events/<slug:slug>',views.eventdetail,name='event-details'),
    path('events/edit/<slug:slug>',EditEventView.as_view(),name='edit-event'),
    path('events/<slug:slug>/remove',DeleteEventView.as_view(),name='delete-event'),
    path("fellowship/",views.fellowship,name="fellowship"),
    path('fellowship/<slug:slug>',views.fellowshipdetail,name='fellowship-details'),
    path('fellowship/edit/<slug:slug>',EditFellowshipView.as_view(),name='edit-fellowship'),
    path('fellowship/<slug:slug>/remove',DeleteFellowshipView.as_view(),name='delete-fellowship'),
    path("hire/",views.hire,name="hire"),
    path('hire/edit/<int:pk>',EditHireView.as_view(), name='edit-hire'),
    path('hire/<int:pk>/remove',DeleteHireView.as_view(),name='delete-hire'),
    path("scholarship/",views.scholarship,name="scholarship"),
    path('scholarship/<slug:slug>',views.scholarshipdetail,name='scholarship-details'),
    path('scholarship/edit/<slug:slug>',EditScholarshipView.as_view(),name='edit-scholarship'),
    path('scholarship/<slug:slug>/remove',DeleteScholarshipView.as_view(),name='delete-scholarship'),
    path("about/",views.about,name="about"),
    path("digiLabs/",views.track,name="track"),
    path('digilabs/<slug:slug>',views.trackdetail,name='track-details'),
    path('digiLabs/edit/<slug:slug>',EditTrackView.as_view(),name='edit-track'),
    path('digiLabs/<slug:slug>/remove',DeleteTrackView.as_view(),name='delete-track'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category',views.CategoryL,name='buy'),
    path('hire_category/<str:cats>/',views.HireCategoryView,name='hirecategory'),
    path('hirecategory',views.HireCategoryL,name='hirecategory'),
    path('add_post/',AddBlogPost.as_view(),name='add-post'),
    path('article/edit/<slug:slug>',UpdatePostView.as_view(),name='update-post'),
    path('article/<slug:slug>/remove',DeletePostView.as_view(),name='delete-post'),
    
    path('blog/',views.blog,name='blog'),
    path('blog/<slug:slug>',views.blogdetail,name='details'),
    path('blog_category/<str:cats>/',views.BlogCategoryView,name='blogcategory'),
    path('blogcategory',views.BlogCategoryL,name='blogcategorylist'),
    path('blog/<slug:slug>/reply/<int:comment_id>/', views.reply, name='reply'),
    

    
   



    


    path("job/",JobView.as_view(),name="job"),
    path('job/<slug:slug>', JobDetailView.as_view() , name='jobdetail'),
    path('job/edit/<slug:slug>',EditJobView.as_view(),name='edit-job'),
    path('job/<slug:slug>/remove',DeleteJobView.as_view(),name='delete-job'),
    path('add_job/',AddJobPost.as_view(),name='add-job'),
    
    path('add_scholarship/',AddScholarshipPost.as_view(),name='add-scholarship'),
    path('add_fellowship/',AddFellowshipPost.as_view(),name='add-fellowship'),
    path('add_digiLabs/',AddTrackPost.as_view(),name='add-track'),
    path('add_event/',AddEventPost.as_view(),name='add-event'),
    path('add_community/',AddCommunityPost.as_view(),name='add-community'),
    path('add_hire/',AddHirePost.as_view(),name='add-hire'),
   



]