from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Blogger


# Create your views here.


def home_view(request:HttpRequest):

    blog=Blogger.objects.all()

    
    return render(request,"main/index.html",{"blog":blog})

def new_post(request:HttpRequest):
    if request.method == "POST":
        new_blog=Blogger(title=request.POST.get["title"],contant=request.POST.get["contant"],is_published=request.POST.get["is_published"],published_at=request.POST.get["published_at"])
        new_blog.save()


    return render(request,"main/post.html")