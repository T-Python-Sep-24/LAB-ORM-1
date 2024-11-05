from django.shortcuts import render,redirect
from datetime import date
from django.http import HttpRequest , HttpResponse 

from .models import Blog

def home_view(request:HttpRequest):

    bolgs = Blog.objects.all()   
    
    return render(request , "main/home.html" , {"blogs":bolgs})

def new_post_view(request:HttpRequest):
    if request.method == "POST":
        obj_blog = Blog(title=request.POST["title"] ,content=request.POST["content"],is_published = True, poster=request.FILES["poster"],category=request.POST["category"])
        obj_blog.save()
    
    return render(request , "main/newpost.html")


def detail_view(request:HttpRequest , blog_id:int):
    try:
        detail_blog = Blog.objects.get(pk=blog_id)

        return render(request , "main/detail.html" ,{"detail_blog":detail_blog})
    except:
        return render(request , "main/error.html")

def update_view(request:HttpRequest , blog_id:int ):
    
    update_blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        update_blog.title = request.POST["title"]
        update_blog.content = request.POST["content"]
        if "poster" in request.FILES:
            update_blog.poster = request.FILES["poster"]
        update_blog.save()
        return redirect("main:detail_view",blog_id = update_blog.id)
    return render(request , "main/update.html", {"update_blog":update_blog})



def delete_view(request:HttpRequest , blog_id:int ):
    
    delete_blog = Blog.objects.get(pk=blog_id)
    delete_blog.delete()
    return redirect("main:home_view")



def error_view(request:HttpRequest):

    return render(request,"main/home.html")