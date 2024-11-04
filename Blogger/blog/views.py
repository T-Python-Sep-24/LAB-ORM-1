from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpRequest,HttpResponse
from .models import Post
from django.utils import timezone


# Create your views here.


def home(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})



def add_post(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=True if request.POST.get("is_published") == "on" else False,
            published_at=request.POST.get("published_at", timezone.now()),
            poster = request.FILES("poster"),
        )
        new_post.save()
        return redirect('home')

    return render(request, "blog/add_post.html" )


def blog_detail_view(request: HttpRequest, blog_id:int):
    post = Post.objects.get(pk=blog_id)
    return render(request, "blog/detail.html", {'post': post})

def blog_update_view(request: HttpRequest, blog_id:int):
    post = Post.objects.get(pk=blog_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = True if request.POST.get("is_published") == "on" else False
        post.published_at = request.POST.get("published_at", timezone.now())
        if "poster" in request.FILES: post.poster=request.FILES["poster"]
        post.save()
        return redirect("blog:blog_detail_view", blog_id=post.id)
    

    return render(request, "blog/update.html", {'post': post})


def blog_delete_view(request: HttpRequest, blog_id:int):
    post = Post.objects.get(pk=blog_id)
    post.delete()
    return redirect('blog:home')


