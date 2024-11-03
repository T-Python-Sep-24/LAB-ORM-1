from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def homepage(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'main/addpage.html', {'form': form})