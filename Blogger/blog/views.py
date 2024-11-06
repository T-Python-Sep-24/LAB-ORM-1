from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from .forms import BlogForm
# Create your views here.

def new_post_view(request:HttpRequest,):
    blog_form=BlogForm()
    new_post=Post()

    if request.method=='POST':
        blog_form=BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form")
    
    return render(request,'blog/blog.html',context={'blog_form':blog_form,'category':new_post.CategoryChoices.choices})


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


def search_blog_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >=3:
        blogs= Post.objects.filter(title__contains=request.GET["search"])
    else:
        blogs=[]

    return render(request,"blog/search_blog.html",context={"blogs":blogs})