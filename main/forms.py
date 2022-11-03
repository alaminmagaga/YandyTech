from django import forms
from .models import Blog,Category,Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Article
<<<<<<< HEAD
        



        fields=('title','slug','author','body','thumb')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'slug':forms.TextInput(attrs={'class':'form-control','style':'width: 60%;'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','style':'width: 60%;'}),
            'thumb':forms.Select(choices=choice_list,attrs={'class':'form-control','style':'width: 60%;'}),
            'body':forms.Textarea(attrs={'class':'form-control' ,'style':'width: 60%;'}),
=======

        fields=('title','slug','author','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder'}),
>>>>>>> refs/remotes/origin/master
          
           
        }

