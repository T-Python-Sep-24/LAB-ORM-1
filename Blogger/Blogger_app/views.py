from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpRequest
from .models import Post
from django.utils import timezone

def homepage(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'Blogger_app/homepage.html', {'posts': posts})

def newPost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST.get('category')
        poster=request.FILES ("poster")
        Post.objects.create(title=title, content=content, category=category, published_at=timezone.now())
        return redirect('Blogger_app:homepage')
    return render(request, 'Blogger_app/newPost.html')


def blogDeatails(request:HttpRequest, blog_id:int):

    blog = get_object_or_404(Post, pk=blog_id) 
    return render(request, "Blogger_app/blogDeatails.html", {"blog1":blog})


 

def blogUpdate(request:HttpRequest, blog_id:int):

    blog = get_object_or_404(Post, pk=blog_id) 

    if request.method == 'POST':
        blog.title=request.POST["title"]
        blog.content=request.POST["content"]
        blog.category=request.POST["category"]
        if "poster" in request.FILES:
            blog.poster= request.FILES["poster"]
        blog.save()

        return redirect("Blogger_app:blogDeatails", blog_id=blog.id)
    

    return render(request, "Blogger_app/blogUpdate.html", {"blog1":blog})


def blogDelete(request:HttpRequest, blog_id:int):

    blog = get_object_or_404(Post, pk=blog_id)
    blog.delete()

    return redirect("Blogger_app:homepage")


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)




