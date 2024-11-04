from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def base(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/base.html", {'posts': posts})

def add_post(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('homepage')
    return render(request, "blog/add_post.html")


def post_list(request: HttpRequest) :
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/post_list.html", {'posts': posts})