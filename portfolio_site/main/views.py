from django.shortcuts import render, redirect
from .models import projectModel, blogPosts

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # Setup Pagination
    p = Paginator(blogPosts.objects.all(), 3)
    page = request.GET.get('page')
    posts = p.get_page(page)
    projects = projectModel.objects.all()
    
    context = {
        'posts': posts,
        'projects': projects
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def post(request, pk):
    post = blogPosts.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('post', pk=post)
    
    context = {
        'post': post,
    }
    return render(request, 'main/post.html', context)

def loadAllPosts(request):
    all_posts = blogPosts.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'main/posts.html', context)

def viewProject(request, pk):
    project = projectModel.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('project', pk=project)
    
    context = {
        'project': project,
    }
    return render(request, 'main/project.html', context)

def loadAllProjects(request):
    projects = projectModel.objects.all()
    
    context = {
        'projects': projects
    }
    return render(request, 'main/projects.html', context)
    





