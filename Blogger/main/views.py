from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def home_view(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "main/index.html", {"posts": posts})


def add_view(request: HttpRequest):
    try:
        if request.method == "POST":
            post = Post(
                title = request.POST["title"], 
                content = request.POST["content"], 
                is_published = bool(request.POST.get("is_published", False)), 
                image = request.FILES["image"],
                category = request.POST["category"]
            )
            post.save()

            return redirect("main:home_view")
    except:
        return redirect("main:home_view")

    return render(request, "main/add.html")


def post_details_view(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(pk = post_id)
    except:
        return redirect("main:not_found_view")

    return render(request, "main/details.html", {"post": post})


def not_found_view(request: HttpRequest):

    return render(request, "main/notfound.html")


def update_view(request: HttpRequest, post_id):
    try:
        # get the post by the id
        post = Post.objects.get(pk = post_id)

        # Check if the form was submited by post method
        if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST["is_published"]
            post.category = request.POST["category"]
            # check if he updated the image
            if "image" in request.FILES:
                post.image = request.FILES["image"]
            post.save()

            # redirect to details pass the id as path param details/id/
            return redirect("main:post_details_view", post_id = post.id)

    except:
        return redirect("main:not_found_view")

    return render(request, "main/update.html", {"post": post})


def delete_view(request: HttpRequest, post_id: int):
    try:
        # get the post by the id
        post = Post.objects.get(pk = post_id)

        post.delete()
    except:
        return redirect("main:not_found_view")

    return redirect("main:home_view")

    