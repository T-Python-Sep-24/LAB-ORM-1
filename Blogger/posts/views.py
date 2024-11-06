from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpRequest
from .models import Post
from .forms import PostForm
# Create your views here.

def add_post_view(request:HttpRequest):

    if request.method=="POST":
        post_form=PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("main:home_page_view")
        else:
            print("not valid form")
            print(post_form.errors)

    return render(request,'posts/add_post.html',{"CategoryChoices":Post.CategoryChoices.choices})


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
            post_form=PostForm(request.POST, request.FILES,instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect("posts:post_detail_view",post_id=post.id)
            else:
                print("not valid form")
                print(post_form.errors)
        else:
            post_form = PostForm(instance=post)
        return render(request,'posts/update_post.html',{"post":post,"CategoryChoices":Post.CategoryChoices.choices})
    
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


def all_posts_view(request:HttpRequest):
    #get all posts
    posts = Post.objects.all().order_by("-published_at")
    return render(request,'posts/all_posts.html',{"posts":posts})


def search_posts_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"])>=3:
        posts=Post.objects.filter(title__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "published_at":
            posts=posts.order_by("-published_at")
    else:
        posts=[]
    return render(request,'posts/search_posts.html',{"posts":posts})