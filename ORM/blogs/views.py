from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Blog

def view_home(request):
    return render(request, 'main/blog.html')

def create_blog(request):
    if request.method == "POST":
        new_blog = Blog(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published = request.POST.get("is_published")=="on",
            published_at=request.POST.get('published_at', None),
            poster=request.FILES["poster"])
            
        new_blog.save()
    return render(request, 'blogs/create.html')


def blog_id(request ,blogID):
    blog = get_object_or_404(Blog, pk=blogID)
    return render(request,"blogs/details.html" , {"blog": blog})

def update(request , blogID):
     blog = get_object_or_404(Blog, pk=blogID)
     if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST.get("content")
        blog.is_published = request.POST.get("is_published", False)== 'on'
        blog.published_at = request.POST.get("published_at")
        blog.poster = request.FILES.get("poster", blog.poster)  
        blog.save()

     return render(request, 'blogs/update.html', {'blog': blog})   


def delete(request, blogID):
    blog = get_object_or_404(Blog, pk=blogID)
    blog.delete()
    return redirect("main:home") 

