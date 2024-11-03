from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from posts.models import Post

# Create your views here.

def index_view(request:HttpRequest):

    #get all posts
    posts = Post.objects.all()

    return render(request, 'main/index.html', {"posts" : posts} )
