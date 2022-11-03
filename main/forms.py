from django import forms
from .models import Blog,Category,Article, Scholarship
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Article


        fields=('title','slug','author','body','thumb')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'slug':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden','style':'width: 60%;'}),
            #'thumb':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'body':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model=Article


        fields=('title','slug','author','body','thumb')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'slug':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
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