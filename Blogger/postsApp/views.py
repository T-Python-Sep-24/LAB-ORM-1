from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def create_post_view(request: HttpRequest):
    # print(request.POST)

    if request.method == "POST":
        new_post = Post(title=request.POST['title'], content=request.POST['content'])
        new_post.save()

        request = redirect('bloggerApp:main_view')
        return request

    request = render(request, 'create_post.html')
    return request