from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone

def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            is_published=True if request.POST.get("is_published") == "on" else False,
            poster=request.FILES["poster"], 
        ) 
        new_post.save()

        return redirect("main:index_view")  

    return render(request, "posts/create.html")
