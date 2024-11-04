from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def create_post_view(request: HttpRequest):
    # print(request.POST)

    if request.method == "POST":
        new_post = Post(title=request.POST['title'], content=request.POST['content'], post_img=request.FILES['post_img'])

        new_post.save()

        request = redirect('bloggerApp:main_view')
        return request

    request = render(request, 'create_post.html')
    return request

def post_details_view(request: HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    request = render(request, 'post_details.html', context={'post': post})
    return request

def update_post_view(request: HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        if 'post_img' in request.FILES: post.post_img = request.FILES['post_img']
        post.save()
        return redirect('postsApp:post_details_view', post_id=post.id)

    request = render(request, 'update_post.html', context={'post': post})
    return request

def delete_post_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect('bloggerApp:main_view')
