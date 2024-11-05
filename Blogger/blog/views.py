from django.shortcuts import render, redirect 
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import Blog 

def post_view(request: HttpRequest):
    if request.method == "POST":

        new_post = Blog(title=request.POST["title"],content=request.POST["content"],image=request.FILES["image"],category=request.POST["category"])
        new_post.save()
        messages.success(request, "Post added successfully!") 
        return redirect("main:home_view")  

    return render(request, "blog/post.html")

        
def post_detail_view(request:HttpRequest, post_id:int):
    
    post = Blog.objects.get(pk =post_id)

    return render(request, "blog/post_detail.html",{"post":post})

    
def post_update_view(request:HttpRequest, post_id:int):

    post = Blog.objects.get(pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()

        messages.success(request, "Post updated successfully!") 
        return redirect("main:home_view")  

    return render(request, "blog/post_update.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id: int):
    post = Blog.objects.get(pk=post_id)
    post.delete()
    
    messages.success(request, "Post deleted successfully.")
    return redirect("main:home_view")
 

def handler500(request,exception):
    return render(request, '500.html')


def handler404(request):
    return render(request, '404.html')