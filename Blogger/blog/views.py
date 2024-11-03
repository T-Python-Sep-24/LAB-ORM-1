from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog


def post_view(request:HttpRequest):

    if request.method=="POST":


        new_blog = Blog(title=request.POST["title"],content=request.POST["content"])
        new_blog.save()
        
    return render(request, "blog/post.html")
    
