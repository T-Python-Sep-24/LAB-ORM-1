from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.utils import timezone

def home(request):
    post_list = Post.objects.filter(is_published=True).order_by('-published_at')
    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'posts/home.html', {
        'posts': posts,
        'current_datetime': timezone.now(),
        'year': timezone.now().year
    })

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_published = True  # Set to True to publish immediately
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'posts/delete_post.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html')

def contact(request):
    return render(request, 'posts/contact.html')
