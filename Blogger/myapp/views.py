from django.shortcuts import render, redirect
from django.utils import timezone
from .models import post
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostForm

def add_post_view(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('myapp:display')
        else:
            print("not valid form")
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # is_published = 'is_published' in request.POST
        # published_at = request.POST.get('published_at') or timezone.now()


    #     new_post = post(
    #         title=title,
    #         content=content,
    #         is_published=is_published,
    #         published_at=published_at,
    #     )

    #     if 'poster' in request.FILES:
    #         new_post.poster = request.FILES.get('poster')

    #     new_post.save()


    #     return redirect('myapp:display')

    # context = {
    #     'current_time': timezone.now().strftime('%Y-%m-%dT%H:%M')
    # }
    return render(request, 'myapp/home.html', {"post_form":post_form})



def display_view(request):
    
    posts = post.objects.filter(is_published=True).order_by('-published_at').filter(title__contains="t").all()[0:14]

    context = {
        'posts': posts
    }
    
    return render(request, 'myapp/display.html', context)

def details_view(request, the_id:int):
    try:
        posts=post.objects.get(pk=the_id)

        return render(request, 'myapp/details.html', {'post': posts})
    
    except ObjectDoesNotExist:
        
        return HttpResponse(f"Post with ID {the_id} does not exist.")


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
    try:
        posts=post.objects.get(pk=the_id)
        posts.delete()
        return redirect("myapp:display")
    
    except ObjectDoesNotExist:

        return HttpResponse(f"Post with ID {the_id} does not exist.")

def search_view(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        posts = post.objects.filter(title__icontains=request.GET["search"]).order_by('-published_at')
    else:
        posts = []    

    return render(request, 'myapp/search.html', {"posts": posts})