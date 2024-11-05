from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
 
def home_view(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-id')
    return render(request, "main/home.html", {"posts": posts})


def create_view(request:HttpRequest):    
    if request.method == "POST":
        new_post = Post(title=request.POST["title"],content=request.POST["description"],category= request.POST["category"])
        if "image" in request.FILES: new_post.image = request.FILES["image"]
        new_post.save()
    return render(request, "main/create.html")

def detail_view(request:HttpRequest,post_id:int):
    try:
        post_detail = Post.objects.get(pk=post_id)
        return render(request,"main/detail.html", {"post_detail":post_detail})
    except Exception as e :
        return render(request,"main/page_not_found.html")

def update_view(request:HttpRequest,post_id:int):
    post_detail = Post.objects.get(pk=post_id)
    if request.method == "POST":
        post_detail.title = request.POST["title"]
        post_detail.content = request.POST["description"]
        post_detail.category = request.POST["category"]
        if "image" in request.FILES: post_detail.image = request.FILES["image"]
        post_detail.save()

        return redirect("main:detail_view",post_id=post_id)
    return render(request,"main/update.html", {"post_detail":post_detail})


def delete_view(request:HttpRequest,post_id:int):
    post_detail = Post.objects.get(pk=post_id)
    post_detail.delete()
    return redirect("main:home_view")