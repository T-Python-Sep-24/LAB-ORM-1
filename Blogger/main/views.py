from django.shortcuts import render
from datetime import date
from django.http import HttpRequest , HttpResponse 

from .models import Blog

def home_view(request:HttpRequest):

    bolgs = Blog.objects.all()    
    
    return render(request , "main/home.html" , {"view":bolgs})

def new_post_view(request:HttpRequest):
    if request.method == "POST":
        obj_blog = Blog(title=request.POST["title"] ,content=request.POST["content"],is_published = True, published_at=date.today())
        obj_blog.save()
    
    return render(request , "main/newpost.html")
