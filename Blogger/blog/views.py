from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.timezone import now
from datetime import datetime
from .models import Blog

def create_blog_view(request:HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published= True if request.POST["is_published"] == "published" else False)
        new_blog.save()
    
    return render(request, "blog/create.html")
     

