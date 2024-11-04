from django.shortcuts import render, redirect
from django.utils import timezone
from .models import post
from django.urls import reverse
from django.http import HttpRequest

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
            published_at=published_at,
        )

        if 'poster' in request.FILES:
            new_post.poster = request.FILES.get('poster')

        new_post.save()


        return redirect('myapp:display')

    context = {
        'current_time': timezone.now().strftime('%Y-%m-%dT%H:%M')
    }
    return render(request, 'myapp/home.html', context)



def display_view(request):
    
    posts = post.objects.filter(is_published=True).order_by('-published_at')

    context = {
        'posts': posts
    }
    return render(request, 'myapp/display.html', context)

def details_view(request, the_id:int):

    posts=post.objects.get(pk=the_id)

    return render(request, 'myapp/details.html', {'post': posts})


def update_view(request:HttpRequest, the_id:int):

    posts=post.objects.get(pk=the_id)

    if request.method =="POST":
        posts.title = request.POST.get("title")
        posts.content = request.POST.get("content")
        posts.is_published = 'is_published' in request.POST
        #posts.published_at = request.POST.get("published_at")
        if "poster" in request.FILES: 
            posts.poster = request.FILES["poster"]
        posts.save()

        return redirect( 'myapp:details_view', the_id=posts.id)

    return render(request, 'myapp/update.html', {'post': posts})

def delete_view(request, the_id:int):

    posts=post.objects.get(pk=the_id)
    posts.delete()
    return redirect("myapp:display")