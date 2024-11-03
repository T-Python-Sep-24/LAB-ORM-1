from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Post


# Create your views here.

def main_view(request: HttpRequest):
    # blogs = [
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    # ]
    blogs = Post.objects.all()
    request = render(request, 'main.html', context={"blogs": blogs})
    return request


def create_post_view(request: HttpRequest):
    print(request.POST)
    if request.method == "POST":
        new_post = Post(title=request.POST['title'], content=request.POST['content'])
        new_post.save()
    request = render(request, 'create_post.html')
    return request