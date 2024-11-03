from django.shortcuts import render, redirect
from django.http import HttpRequest
from post.models import Post

#Post page
def newPostView(request: HttpRequest):
    #Create a new post with user input
    if request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"], isPublished=request.POST["isPublished"], publishedAt=request.POST["publishedAt"])
        post.save()

    return render(request, 'post/post.html')