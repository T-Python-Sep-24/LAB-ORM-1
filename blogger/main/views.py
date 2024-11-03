from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone



def main_view(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'main/main.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=True,
            published_at=timezone.now()
        )
        new_post.save()  


    return render(request, "main/add_post.html")