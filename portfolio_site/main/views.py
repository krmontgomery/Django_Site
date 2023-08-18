from django.shortcuts import render, redirect
from .models import projectModel, blogPosts, aboutModel, aboutExperienceModel

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # Setup Pagination
    blog_p = Paginator(blogPosts.objects.all(), 3)
    page = request.GET.get('page')
    posts = blog_p.get_page(page)
    
    project_p = projectModel.objects.filter().order_by('-id')[:3][::-1]
    
    context = {
        'posts': posts,
        'project_p': project_p,
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def post(request, pk):
    p = Paginator(blogPosts.objects.exclude(id=pk), 3)
    page = request.GET.get('page')
    posts = p.get_page(page)
    post = blogPosts.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('post', pk=post)
    
    context = {
        'post': post,
        'posts': posts
    }
    return render(request, 'main/post.html', context)

def loadAllPosts(request):
    all_posts = blogPosts.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'main/posts.html', context)

def viewProject(request, pk):
    projects = projectModel.objects.exclude(id=pk)
    project = projectModel.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('project', pk=project)
    context = {
        'project': project,
        'projects': projects,
    }
    return render(request, 'main/project.html', context)

def loadAllProjects(request):
    projects = projectModel.objects.all()
    
    context = {
        'projects': projects
    }
    return render(request, 'main/projects.html', context)

def loadJobExperience(request):
    experience = aboutExperienceModel.objects.all()
    context = {
        'experience': experience
    }
    return render(request, 'main/about.html', context)




