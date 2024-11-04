from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def home_view(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "main/index.html", {"posts": posts})


def add_view(request: HttpRequest):
    if request.method == "POST":
        post = Post(title = request.POST["title"], content = request.POST["content"], is_published = bool(request.POST.get("is_published", False)))
        post.save()

    return render(request, "main/add.html")