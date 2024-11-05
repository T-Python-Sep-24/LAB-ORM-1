from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            category=request.POST.get("category"),
            poster=request.FILES["poster"], 
            is_published=True if request.POST.get("is_published") == "on" else False,
        ) 
        new_post.save()

        return redirect("main:index_view")  

    return render(request, "posts/create.html")


def post_detail_view(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
    except Http404:
        return render(request, 'posts/404.html', status=404)
    return render(request, 'posts/post_detail.html', {"post": post})


def post_update_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category=request.POST["category"]
        if "poster" in request.FILES: post.poster = request.FILES["poster"]
        post.is_published = request.POST.get('is_published', 'off') == 'on'
        post.save()
        
        return redirect("posts:post_detail_view", post_id=post.id)

    return render(request, "posts/post_update.html", {"post":post})


def post_delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:index_view")


def custom_404_view(request, exception):
    return render(request, "posts/404.html", status=404)


def all_posts_view(request:HttpRequest):
    #posts = Post.objects.filter(is_published__gte=3).order_by("-published_at")
    #posts = Post.objects.filter(is_published__gte=True).exclude(title__contains="AI").order_by("-published_at")
    #posts = Post.objects.all().order_by("-published_at")
    #results count
    #print(posts.count())
    
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/all_posts.html", {'page_obj': page_obj})











