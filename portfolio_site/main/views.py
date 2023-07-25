from django.shortcuts import render, redirect
from .models import projectModel, blogPosts

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # posts = blogPosts.objects.all()
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

def post(request, pk):
    post = blogPosts.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('post', pk=post)
    
    context = {
        'post': post,
    }
    print(context)
    return render(request, 'main/post.html', context)
    






