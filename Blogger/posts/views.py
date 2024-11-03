from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone

def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            is_published=True if request.POST.get("is_published") == "on" else False,  # Convert "on" to True
            published_at=request.POST.get("published_at") or timezone.now(),  # Use current time if not provided
        ) 
        new_post.save()

        return redirect("main:index_view")  # Make sure "index" is the correct URL name for the home page

    return render(request, "posts/create.html")
