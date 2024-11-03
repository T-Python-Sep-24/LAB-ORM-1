from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
 
def home_view(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "main/home.html", {"posts": posts})


def create_view(request:HttpRequest):
    print(request.POST)
    if request.method == "POST":
        new_post = Post(title=request.POST["title"],content=request.POST["description"],is_published=True,published_at=datetime.now())
        new_post.save()
    return render(request, "main/create.html")
