from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def home_view(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "main/index.html", {"posts": posts})


def add_view(request: HttpRequest):
    if request.method == "POST":
        post = Post(title = request.POST["title"], content = request.POST["content"], is_published = bool(request.POST.get("is_published", False)), image = request.FILES["image"])
        post.save()

        return redirect("main:home_view")

    return render(request, "main/add.html")
