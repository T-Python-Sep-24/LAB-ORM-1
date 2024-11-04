from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
# Create your views here.
def new_post_view(request:HttpRequest,):
    if request.method=='POST':
        new_post=Post(title=request.POST['title'],content=request.POST['content'])
        new_post.save()
    
    return render(request,'blog/blog.html')