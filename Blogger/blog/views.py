from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from datetime import datetime

def create_blog_view(request:HttpRequest):
    if request.method == "POST":
        if request.POST["is_published"] == "published":
            published = True
        else:
            published = False
        if "poster" in request.FILES:  
            new_blog = Blog(category=request.POST["category"], title=request.POST["title"], content=request.POST["content"], is_published= published, poster=request.FILES["poster"]) 
        else:
            new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published= published) 
            
        new_blog.save()
        return redirect("blog:blog_view", blog_id=new_blog.id)
    
    return render(request, "blog/create.html")

def blog_view(request: HttpRequest, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    return render(request, "blog/blog.html", {"blog": blog})

def update_blog_view(request: HttpRequest, blog_id:int):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST['content']
        
        if "ispublished" in request.POST:
            if request.POST["ispublished"] == "published":
                published = True
            else:
                published = False
            blog.is_published = published
        
        blog.category = request.POST["category"]
    
        if "poster" in request.FILES:
            blog.poster = request.FILES["poster"]
            
        blog.save()
        
        return redirect("blog:blog_view", blog_id=blog_id)
    
    return render(request, "blog/update.html", {"blog": blog})

def delete_blog_view(request: HttpRequest, blog_id:int):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
      
    return redirect("main:home_view")
    
     

