from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from posts.models import Post


# Create your views here.

def index_view(request: HttpRequest):
    
    #posts = Post.objects.filter(is_published__gte=3).order_by("-published_at")
    #posts = Post.objects.all().order_by("-published_at")
    #get all posts
    posts = Post.objects.all()
    
    posts = Post.objects.filter(is_published__gte=True).exclude(title__contains="AI").order_by("-published_at")
    
    #results count
    print(posts.count())
    
    return render(request, 'main/index.html', {"posts" : posts} )
