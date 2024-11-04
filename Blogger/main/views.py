from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Blogger
from  datetime import datetime


# Create your views here.


def home_view(request:HttpRequest):

    blog=Blogger.objects.all()

    
    return render(request,"main/index.html",{"blog":blog})

def new_post(request:HttpRequest):

    if request.method == "POST":
      
        new_blog=Blogger(titel=request.POST["titel"],contant=request.POST["contant"],is_published=True,published_at=datetime.now(), poster=request.FILES["poster"])
        new_blog.save()

        return redirect('main:home_view')


    return render(request,"main/post.html")




def post_detail(request:HttpRequest, post_id:int):

    post= Blogger.objects.get(pk=post_id)
    
    
    return render(request,"main/post_detail.html", {"post" : post})


def post_update(request:HttpRequest,post_id):

     post= Blogger.objects.get(pk=post_id)
     if request.method == "POST":
         post.titel = request.POST["titel"]
         post.contant = request.POST["contant"]
         post.is_published = request.POST["is_published"]
         post.published_at = request.POST["published_at"]
         if "poster" in request.FILES: post.poster = request.FILES["poster"]
         post.save()

         return redirect("main:post_detail", post_id=post.id)

     return render(request, "main/post_update.html", {"post" : post})


def post_delete(request:HttpRequest,post_id):

     post= Blogger.objects.get(pk=post_id)
     post.delete()
     return redirect('main:home_view')
