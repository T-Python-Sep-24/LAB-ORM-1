from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone

def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            category=request.POST.get("category"),
            poster=request.FILES["poster"], 
            is_published=True if request.POST.get("is_published") == "on" else False,
        ) 
        new_post.save()

        return redirect("main:index_view")  

    return render(request, "posts/create.html")


def post_detail_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    return render(request, 'posts/post_detail.html', {"post" : post})


def post_update_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category=request.POST["category"]
        if "poster" in request.FILES: post.poster = request.FILES["poster"]
        post.is_published = request.POST.get('is_published', 'off') == 'on'
        post.save()
        
        return redirect("posts:post_detail_view", post_id=post.id)

    return render(request, "posts/post_update.html", {"post":post})


def post_delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:index_view")
