from django import forms
from .models import Blog,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Blog

        fields=('title','sub_title','author','category','body','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }