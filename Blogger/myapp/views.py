from django.shortcuts import render, redirect
from django.utils import timezone
from .models import post
from django.urls import reverse

def add_post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = 'is_published' in request.POST
        published_at = request.POST.get('published_at') or timezone.now()

        new_post = post(
            title=title,
            content=content,
            is_published=is_published,
            published_at=published_at
        )
        new_post.save()

        return redirect(reverse('home'))

    context = {
        'current_time': timezone.now().strftime('%Y-%m-%dT%H:%M')
    }
    return render(request, 'myapp/home.html', context)


def display_view(request):
    # Get all posts ordered by published_at in descending order (latest first)
    posts = post.objects.filter(is_published=True).order_by('-published_at')

    context = {
        'posts': posts
    }
    return render(request, 'myapp/display.html', context)
