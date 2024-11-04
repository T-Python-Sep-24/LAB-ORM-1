from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpRequest,HttpResponse
from .models import Post
from django.utils import timezone


# Create your views here.


def home(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})



def add_post(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=True if request.POST.get("is_published") == "on" else False,
            published_at=request.POST.get("published_at", timezone.now()),
        )
        new_post.save()
        return redirect('home')

    return render(request, "blog/add_post.html" )

