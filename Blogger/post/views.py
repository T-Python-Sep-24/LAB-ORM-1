from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from post.models import Post

#New post page
def newPostView(request: HttpRequest):
    #Create a new post with user input
    categories=Post.CATEGORIES
    response = render(request, 'post/postCreate.html', context={'categories':categories})
    if request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"])
        if "picture" in request.FILES: post.picture = request.FILES["picture"]
        post.save()
        response = redirect('main:homeView')

    return response

#Post details page
def postDetailsView(request: HttpRequest, postid:int):

    post = Post.objects.get(pk=postid)

    return render(request, 'post/postDetails.html', context={"post":post})

#Update post page
def updatePostView(request: HttpRequest, postid:int):
    #Update an existing post with user input
    post = Post.objects.get(pk=postid)
    categories = Post.CATEGORIES
    response = render(request, 'post/postUpdate.html', context={"post":post, "categories":categories})
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        if "picture" in request.FILES: post.picture = request.FILES["picture"]
        post.save()    

        response = redirect('post:postDetailsView', postid=post.id)

    return response

#Delete post page
def deletePostView(request: HttpRequest, postid:int):
    #Delete an existing post
    post = Post.objects.get(pk=postid)
    post.delete()
    
    return redirect('main:homeView')
