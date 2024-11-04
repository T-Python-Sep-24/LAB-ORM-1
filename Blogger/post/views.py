from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from post.models import Post
from django.shortcuts import resolve_url


#Post page
def newPostView(request: HttpRequest):
    #Create a new post with user input
    response = render(request, 'post/post.html')
    if request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"], picture=request.FILES["picture"])
        post.save()
        response = redirect('main:mainView')

    return response