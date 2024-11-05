from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
#from .form import PostForm

from .models import Blog

# Create your views here.


def main_view(request: HttpRequest):

    posts = Blog.objects.all().order_by("-published_at")

    return render(request, "main/home.html", {"posts": posts})




def new_posts_view(request: HttpRequest):

    if request.method == "POST":
        #post_form = PostForm(request.POST, request.FILES)
        #if post_form.is_valid():
            #post_form.save()
            #return redirect("main:post_published_view")
        
        #else:
            #print("Not Valid Form")

        new_post = Blog(
            title=request.POST["title"],
            main_photo=request.FILES["main_photo"],
            content=request.POST["content"],
            category= request.POST["category"]
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
        posts.category=request.POST["category"]

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




def post_all_view(request:HttpRequest):

    posts = Blog.objects.all()

    
    return render(request, 'main/post_all.html', {"posts": posts})




def search_post_view(request:HttpRequest):
    if "search"  in request.GET and len(request.GET["search"]) >= 3:
        posts = Blog.objects.filter(title__contains=request.GET["search"])
    else:
        posts = []    


    
    return render(request, 'main/search_post.html', {"posts": posts})