from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Post
# Create your views here.
def new_post_view(request:HttpRequest,):
    if request.method=='POST':
        new_post=Post(title=request.POST['title'],content=request.POST['content'],image=request.FILES['image'])
        new_post.save()
        return redirect('main:home_view')
    
    return render(request,'blog/blog.html')


def blog_content_view(request:HttpRequest,blog_id:int):
    
    blog=Post.objects.get(pk=blog_id)

    return render(request,'blog/blog_content.html',context={'blog':blog})


def blog_update_view(request:HttpRequest,blog_id:int):
    
    blog=Post.objects.get(pk=blog_id)

    return render(request,'blog/update_blog.html',context={'blog':blog})


def blog_delete_view(request:HttpRequest,blog_id:int):

    blog=Post.objects.get(pk=blog_id)
    blog.delete()
    return redirect('main:home_view')