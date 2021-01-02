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
    num_Category = Category.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def User_posts(request):
    latest_posts = Post.objects.all()
    return render(request,'User_posts')



class ThreadForumList(generic.ListView):
    model = ThreadForum
    context_object_name = 'my_threads_list'  # your own name for the list as a template variable
    queryset = ThreadForum.Thread_forum_id
    template_name = 'threads_in_forum/list_of_threads.html'  # Specify your own template name/location

    class Meta:
        ordering = ['ThreadForum']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ThreadForumList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
