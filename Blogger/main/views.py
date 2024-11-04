from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Blog

def home_view(request: HttpRequest):
    blog = Blog.objects.all()
    return render(request, "main/home.html", {"blog": blog})

def blog_view(request: HttpRequest, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    return render(request, "main/blog.html", {"blog": blog})

