from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.timezone import now
from datetime import date
from .models import Blog

def create_blog_view(request:HttpRequest):
    if request.method == "POST":
        if request.POST["is_published"] == "published":
            published = True
        else:
            published = False
        if "poster" in request.FILES:  
            new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published= published, poster=request.FILES["poster"]) 
        else:
            new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published= published) 
            
        new_blog.save()
    
    return render(request, "blog/create.html")
     

