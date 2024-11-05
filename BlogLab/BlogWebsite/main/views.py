from django.shortcuts import render ,redirect 
from django.http import HttpRequest , HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def home_view(request:HttpRequest):
    posts=Post.objects.all()
    return render(request,"main/home.html",{'posts':posts})

def addPost_view (request : HttpRequest):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  
        post = Post(title=title, content=content, published_at=timezone.now(),image=request.FILES["image"])
        post.save()
        return redirect('main:home_view')  
    return render(request, 'main/addPost.html')

def DetailPage_view(request : HttpRequest , post_id:int):
    post = Post.objects.get(pk=post_id)
    return render(request, 'main/DetailPage.html', context={"post" :post})

def post_update_view(request :HttpRequest,post_id:int):
    post = Post.objects.get(pk=post_id)

    if request.method =="POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.published_at = request.POST["published_at"]
        if "image" in request.FILES: post.image = request.FILES["image"]
        post.save()
        return redirect("main:DetailPage_view " , post_id= post.id )
    return render(request,"main/post_update.html", context={"post":post})

def post_delete_view(request :HttpRequest,post_id:int):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")
