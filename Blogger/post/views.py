from django.shortcuts import render, redirect
from django.http import HttpRequest
from post.models import Post
from .forms import PostForm

#New post page
def newPostView(request: HttpRequest):
    #Create a new post with user input
    postData = PostForm()

    response = render(request, 'post/postCreate.html', context={'categories':Post.Categories.choices})
    
    if request.method == "POST":
        postData = PostForm(request.POST)
        if postData.is_valid():
        # post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"])
        # if "picture" in request.FILES: post.picture = request.FILES["picture"]
            postData.save()
        response = redirect('main:homeView')

    return response

#Post details page
def postDetailsView(request: HttpRequest, postid:int):
    #Check if the ID is valid or display a 404
    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = redirect('main:notFoundView')
    else:
        response = render(request, 'post/postDetails.html', context={"post":post})
    
    return response

#Update post page
def updatePostView(request: HttpRequest, postid:int):

    #Update an existing post with user input, display 404 if invalid id entered in url
    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = redirect('main:notFoundView')
    else:
    #Get the category choices and send it in context
        categories = Post.Categories.choices
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
    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = redirect('main:notFoundView')
    else:
        post.delete()
        response = redirect('main:homeView')
    return response

#Filter by category
def categoryFilterView(request: HttpRequest, category):

    posts = Post.objects.filter(category=category)
    response = render(request, 'post/allPosts.html', context={'posts': posts, 'categories': Post.Categories.choices, 'selected': category})
    return response

#Display all posts page
def allView(request: HttpRequest):
    
    categories = Post.Categories.choices
    #Get the list of posts
    posts = Post.objects.all().order_by("-publishedAt")[0:3]

    return render(request, 'post/allPosts.html', context={'posts': posts, 'categories': categories})

