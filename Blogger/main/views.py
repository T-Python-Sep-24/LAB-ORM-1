from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from.models import Blog

# Create your views here.

def main_view(request:HttpRequest):

    if request.method == "POST":
        new_post = Blog(title=request.POST["title"], main_photo=request.POST["main_photo"], content=request.POST["content"])
        new_post.save()
    else:
        print("Error")
        
    posts = Blog.objects.all()   

    return render(request, "main/home.html", {"posts" : posts})



def new_posts_view(request:HttpRequest):

    return render(request, "main/new_post.html")

