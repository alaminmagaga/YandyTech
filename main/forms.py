from django import forms
from .models import Category,Article, Scholarship,Fellowship,Event,Hire,Track,Job,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Article


        fields=('title','author','body','thumb')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
   
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden','style':'width: 60%;'}),
            #'thumb':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'body':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model=Article


        fields=('title','author','body','thumb')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
         
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','style':'width: 50%;'}),
            #'thumb':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'body':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model=Scholarship


        fields=('image','title','description','website','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }

class EditScholarship(forms.ModelForm):
    class Meta:
        model=Scholarship


        fields=('image','title','description','website','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }





class FellowshipForm(forms.ModelForm):
    class Meta:
        model=Fellowship


        fields=('image','title','description','website','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }

class EditFellowship(forms.ModelForm):
    class Meta:
        model=Fellowship


        fields=('image','title','description','website','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }


    
class TrackForm(forms.ModelForm):
    class Meta:
        model=Track


        fields=('image','title','description','link','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'link':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }

 
class EditTrack(forms.ModelForm):
    class Meta:
        model=Track


        fields=('image','title','description','link','deadline')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'link':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }



class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=('image','title','description','website','deadline','eventdate','location')
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'eventdate':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }


  
 
class EditEvent(forms.ModelForm):
    class Meta:
        model=Event
        fields=('image','title','description','website','deadline','eventdate','location')
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'eventdate':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }


    
   

   


class HireForm(forms.ModelForm):
    class Meta:
        model=Hire
        fields=('name','skills','description','website','twitter','facebook','linkedin','instagram','category')
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'skills':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'twitter':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'facebook':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'instagram':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'eventdate':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }


  
 
class EditHire(forms.ModelForm):
    class Meta:
        model=Hire
        fields=('name','skills','description','website','twitter','facebook','linkedin','instagram','category')
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'skills':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'twitter':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'facebook':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'instagram':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'website':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'eventdate':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }



class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=('position','company','amount','number','women','deadline','category','link','description','location','image')
        
        widgets={
            'position':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'company':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'amount':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'number':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'women':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'link':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }



  
 
class EditJob(forms.ModelForm):
    class Meta:
        model=Job
        fields=('position','company','amount','number','women','deadline','category','link','description','location')
        
        widgets={
            'position':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'company':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'amount':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'number':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'women':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'deadline':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'link':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'description':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
            'location':forms.TextInput(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }




# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'body']
#         labels = {'name': 'Name', 'email': 'Email', 'body': 'Comment'}
#         widgets = {'body': forms.Textarea(attrs={'rows': 5})}



class CommentForm(forms.ModelForm):
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'parent')
