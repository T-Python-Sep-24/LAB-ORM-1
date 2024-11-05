from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
# Create your views here.
def new_post_view(request:HttpRequest,):
    new_post=Post()
    if request.method=='POST':
        new_post=Post(title=request.POST['title'],content=request.POST['content'],image=request.FILES['image'],category=request.POST['category'])
        new_post.save()
        return redirect('main:home_view')
    
    return render(request,'blog/blog.html',context={'category':new_post.CategoryChoices.choices})


def blog_content_view(request:HttpRequest,blog_id:int):

    try:
        blog=Post.objects.get(pk=blog_id)

        return render(request,'blog/blog_content.html',context={'blog':blog})
    except Post.DoesNotExist :
        return redirect('main:error_view')


def blog_update_view(request:HttpRequest,blog_id:int):
    try:
        blog=Post.objects.get(pk=blog_id)
        
        if request.method=='POST':
            blog.title=request.POST['title']
            blog.category=request.POST['category']
            blog.content=request.POST['content']
            if "image" in request.FILES: blog.image=request.FILES['image']
            blog.save()
            
            return redirect('blog:blog_content_view',blog_id=blog.id)

        return render(request,'blog/update_blog.html',context={'blog':blog,'category':Post.CategoryChoices.choices})
    except Post.DoesNotExist:
        return redirect('main:error_view')


def blog_delete_view(request:HttpRequest,blog_id:int):

    blog=Post.objects.get(pk=blog_id)
    blog.delete()
    return redirect('main:home_view')