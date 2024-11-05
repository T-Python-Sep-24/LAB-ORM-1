from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpRequest
from .models import Post

# Create your views here.

def add_post_view(request:HttpRequest):
    if request.method=="POST":
        new_post=Post(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],poster=request.FILES.get("poster",default="images/default.jpg"),category=request.POST['category'])
        new_post.save()
        return redirect("main:home_page_view")
    return render(request,'posts/add_post.html')

def post_detail_view(request:HttpRequest,post_id:int):

    try:
        post =Post.objects.get(pk=post_id)
        return render(request,'posts/post_details.html',{"post":post})
    except Post.DoesNotExist:
        return redirect('posts:notfound_view')
    except Exception as e:
        raise f"{e}: there is something wrong"


def post_update_view(request:HttpRequest,post_id:int):
    try:
        post =Post.objects.get(pk=post_id)

        if request.method=="POST":
            post.title=request.POST['title']
            post.content=request.POST['content']
            post.published_at=request.POST["published_at"]
            post.is_published=request.POST['is_published']
            post.category=request.POST['category']
            if "poster" in request.FILES: 
                post.poster =request.FILES["poster"]
            post.save()

            return redirect("posts:post_detail_view",post_id=post.id)

        return render(request,'posts/update_post.html',{"post":post})
    
    except Post.DoesNotExist:
        return redirect('posts:notfound_view')
    except Exception as e:
        raise f"{e}: there is something wrong"

def post_delete_view(request:HttpRequest,post_id:int):
    try:
        post =Post.objects.get(pk=post_id)
        post.delete()

        return redirect("main:home_page_view")
    except Post.DoesNotExist:
        return redirect('posts:notfound_view')
    except Exception as e:
        raise f"{e}: there is something wrong"


def notfound_view(request:HttpRequest):
    return render(request,'posts/notfound_page.html')
