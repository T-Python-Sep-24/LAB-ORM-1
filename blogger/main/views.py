from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from django.http import Http404




def main_view(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'main/main.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        new_post = Post(
            poster=request.FILES["poster"],
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=True
        )
        new_post.save()  


    return render(request, "main/add_post.html")


def blog_detail_view(request, blog_id: int):  
    post = get_object_or_404(Post, pk=blog_id) 
    return render(request, 'main/blog_detail.html', {"post": post})


def update_post(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        
        if "poster" in request.FILES:
            post.poster = request.FILES["poster"]

        post.save()
        return redirect('main:main')
    return render(request, "main/update_post.html", {"post": post})




def delete_post(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    post.delete()
    return redirect('main:main')


from django.shortcuts import render

def custom_view(request, exception):
    return render(request, 'main/404.html', status=404)
