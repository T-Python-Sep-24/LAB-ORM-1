from django.shortcuts import render, redirect
from django.http import HttpRequest
from post.models import Post

#Home page
def homeView(request: HttpRequest):
    #Get the list of posts
    posts = Post.objects.all()

    return render(request, 'main/home.html', context={'posts': posts})
