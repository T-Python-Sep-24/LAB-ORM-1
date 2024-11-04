from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .models import Blog

# Create your views here.


def main_view(request: HttpRequest):

    posts = Blog.objects.all()

    return render(request, "main/home.html", {"posts": posts})




def new_posts_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Blog(
            title=request.POST["title"],
            main_photo=request.FILES["main_photo"],
            content=request.POST["content"]
            )
        
        new_post.save()

        return redirect("main:post_published_view")

    return render(request, "main/new_post.html")




def post_detail_view(request: HttpRequest, post_id:int):

    try:
        posts = Blog.objects.get(pk=post_id)

    except Blog.DoesNotExist:
        return render(request, "main/page_not_found.html", status=404)    

    return render(request, "main/post_detail.html", {"post": posts})




def post_update_view(request: HttpRequest, post_id:int):

    posts = Blog.objects.get(pk=post_id)

    if request.method == "POST":
        posts.title = request.POST["title"]
        if "pomain_photost" in request.FILES: posts.main_photo=request.FILES["main_photo"],
        posts.content=request.POST["content"]

        posts.save()

        return redirect("main:post_success_updated_view", post_id=posts.id)

    return render(request, "main/post_update.html", {"post": posts})




def post_delete_view(request: HttpRequest, post_id:int):

    posts = Blog.objects.get(pk=post_id)
    posts.delete()

    return redirect("main:main_view")

    #return render(request, "main/home.html", {"post": posts}) 




def post_published_view(request:HttpRequest):

    return render(request, 'main/post_published_success.html')




def post_success_updated_view(request:HttpRequest, post_id:int):
    
    posts = Blog.objects.get(pk=post_id)

    
    return render(request, 'main/post_updated_success.html', {"post": posts})

