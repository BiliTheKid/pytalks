from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
""""
home: This is the home page that takes all forums and discussion
objects and passes them to the template through a 
dictionary named context. This page links to both the other pages and 
shows all the required information to the user with the feature of adding more
information in any forum.


"""
def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'home.html', context)


def addInForum(request):
    form_class = CreateInForum
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInDiscussion.html', context)


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def New_Discussion(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'New_Discussion.html')

