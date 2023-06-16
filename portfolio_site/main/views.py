from django.shortcuts import render, redirect
from .models import testModel, blogPosts

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # posts = blogPosts.objects.all()
    # Setup Pagination
    p = Paginator(blogPosts.objects.all(), 2)
    page = request.GET.get('page')
    posts = p.get_page(page)
    
    context = {
        'posts': posts
    }
    return render(request, 'main/home.html', context)

# def post(request, pk):
#     post_id = blogPosts.objects.get(id=pk)
#     post = blogPosts.objects.all()
    

def post(request, pk):
    post = blogPosts.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('post', pk=post)
    
    context = {
        'post': post
    }
    print(context)
    return render(request, 'main/post.html', context)
    






