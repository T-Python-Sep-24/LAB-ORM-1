from django.shortcuts import render
from django.http import HttpRequest
from blog.models import Blog

def home_view(request: HttpRequest):
    
    blog = Blog.objects.all()
    return render(request, 'main/home.html', {"blog": blog})


def search_view(request: HttpRequest):
    search_title = request.GET.get('title')
    if search_title:
        blog_posts = Blog.objects.filter(title__icontains=search_title)
    else:
        blog_posts = Blog.objects.all()

    return render(request, "main/home.html", {'blog': blog_posts})
