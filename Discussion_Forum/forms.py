from django.forms import ModelForm
from django import forms
from .models import *


class CreateInForum(forms.ModelForm):
    class Meta:
        model = forum
        #fields = "__all__"
        fields = ('name','email','topic','description','link')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'})
        }


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
