from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Post
# Create your views here.

def add_post_view(request:HttpRequest):

    if request.method=="POST":
        new_post=Post(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'])
        new_post.save()
    return render(request,'posts/add_post.html')