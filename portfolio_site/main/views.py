from django.shortcuts import render, redirect
from .models import homeModel, projectModel, blogPosts, aboutModel, aboutExperienceModel
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # Setup Pagination
    home_content = homeModel.objects.all()
    blog_p = blogPosts.objects.filter().order_by('-id')[:3][::-1]
    project_p = projectModel.objects.filter().order_by('-id')[:3][::-1]
    
    context = {
        'home_content': home_content,
        'blog_p': blog_p,
        'project_p': project_p,
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def post(request, pk):
    posts = blogPosts.objects.exclude(id=pk).order_by('-id')[:3][::-1]
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
    projects = projectModel.objects.exclude(id=pk).order_by('-id')[:3][::-1]
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
    about_user = aboutModel.objects.all()
    experience = aboutExperienceModel.objects.all()
    context = {
        'about_user': about_user,
        'experience': experience
    }
    return render(request, 'main/about.html', context)




