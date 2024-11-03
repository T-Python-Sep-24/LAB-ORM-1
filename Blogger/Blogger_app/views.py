from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def homepage(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'Blogger_app/homepage.html', {'posts': posts})

def newPost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, published_at=timezone.now())
        return redirect('homepage')
    return render(request, 'Blogger_app/newPost.html')




